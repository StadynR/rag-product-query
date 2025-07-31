from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import ChatOllama, OllamaEmbeddings
import os

load_dotenv()

OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "")
DATA_FOLDER = os.getenv("DOCUMENTS_FOLDER", "data")

class RetrieverAgent:
    def __init__(self):
        self.vectorstore = self._build_vectorstore()

    def _build_vectorstore(self):
        # Load documents
        docs = []
        data_folder = DATA_FOLDER
        for fname in os.listdir(data_folder):
            if fname.endswith(".txt"):
                loader = TextLoader(os.path.join(data_folder, fname))
                docs.extend(loader.load())

        # Split into chunks
        splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = splitter.split_documents(docs)

        # Embed
        print(f"Connecting to Ollama at: {OLLAMA_URL}")
        embeddings = OllamaEmbeddings(model=OLLAMA_MODEL, base_url=OLLAMA_URL)

        # Index in memory
        vectorstore = Chroma.from_documents(docs, embeddings, collection_name="product_docs")
        return vectorstore

    def retrieve(self, query: str, top_k: int) -> list:
        docs = self.vectorstore.similarity_search(query, k=top_k)
        return [doc.page_content for doc in docs]


class ResponderAgent:
    def __init__(self, prompt:str):
        print(f"Connecting to Ollama at: {OLLAMA_URL}")
        self.llm = ChatOllama(model=OLLAMA_MODEL, temperature=0, base_url=OLLAMA_URL)  # Using Ollama for self-hosted LLM
        self.prompt = PromptTemplate.from_template(prompt)
        self.chain = self.prompt | self.llm | StrOutputParser()

    def generate(self, query: str, context_docs: list[str]) -> str:
        context = "\n".join(context_docs)
        return self.chain.invoke({"context": context, "query": query})
