import argparse
import requests

parser = argparse.ArgumentParser(description="Send a query to the product RAG bot")
parser.add_argument("-q", "--query", required=True, type=str, help="The question to send")
args = parser.parse_args()


url = "http://localhost:8000/query"
payload = {
    "user_id": "user_demo",
    "query": args.query
}

response = requests.post(url, json=payload)
if response.ok:
    print("App's response:")
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")
