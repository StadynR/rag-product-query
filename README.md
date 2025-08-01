# RAG Product Query Bot

This repository provides a Retrieval-Augmented Generation (RAG) bot for answering questions about store products using only the provided context. It uses FastAPI for the backend and integrates with Ollama for LLM inference.

## Features

- Answers product-related questions using only the provided data.
- Integrates with Ollama for LLM responses.
- Dockerized for easy setup and deployment.
- Includes a script for sending queries to the API.

## Setup Instructions
## Data Folder

The `data/` folder contains mock product `.txt` files for testing and demonstration purposes. If you want to use the bot with your own products, replace or add `.txt` files in the `data/` directory. Each file should contain relevant product information in plain text.

### 1. Clone the Repository

```bash
git clone https://github.com/StadynR/rag-product-query.git
cd rag-product-query
```

### 2. Configure Environment Variables

Copy `.env.example` to `.env` and adjust values as needed:

**Windows:**
```powershell
copy .env.example .env
```
**Linux:**
```bash
cp .env.example .env
```

Set the following variables in `.env`:

- `TOP_K`: Number of top documents to retrieve.
- `OLLAMA_MODEL`: Ollama model name (e.g., llama3.1).
- `OLLAMA_MODELS_PATH`: Path to Ollama models.
- `DOCUMENTS_FOLDER`: Path to product data.

### 3. Build and Start with Docker Compose

```bash
docker compose up --build
```

This will start:
- Ollama (LLM backend)
- RAG app (API server on port 8000)
- Test service (runs pytest)

## Running Locally (without Docker)

1. Create and activate a Python virtual environment:

**Windows:**
```powershell
python -m venv rag-product-venv
rag-product-venv\Scripts\Activate.ps1
```
**Linux:**
```bash
python3 -m venv rag-product-venv
source rag-product-venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Start the API server:

```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

## Sending a Query to the API

You can use the provided `post_to_app.py` script to send a POST request to the running API.

### Usage (Use `python3` in Linux)

```bash
python3 post_to_app.py -q "<query>"
```

- Replace the query string with your question.
- The script will print the answer and the documents used for the response.

### Example 1

```bash
python3 post_to_app.py -q "Does UNO come with instructions?"
```

#### Output

```
OK response:
User ID: user_demo
Answer: Yes, the UNO game comes with instructions. According to the product description, it includes "108 cards + instructions".
------------------Documents used:-----------------------
Product:Pandemic
Description: Cooperative strategy game where players act as disease‑fighting specialists working together to treat outbreaks and discover cures for four deadly diseases before time runs out. Players either all win or all lose together.
Ages: 8+ years
Players: 2 to 4 players
Contents: World map game board, role cards, pawns, disease cubes, infection cards, player cards, research station pieces, reference cards, rulebook
Price: $49.99
Available: Yes
--------------
Product:UNO
Description: A colorful and addictive card game where players must get rid of their cards by matching them by color or number. Includes special cards (Skip, Reverse, Draw Two, Wild, Wild Draw Four). Perfect for quick games and family fun.
Ages: 7+ years
Players: 2 to 10 players
Contents: 108 cards + instructions
Price: $8.99
Available: Yes
--------------
Product:Catan
Description: Trade and building game set on a resource-rich island. Players collect brick, wood, sheep, wheat, and ore to build settlements, cities, and roads. Involves negotiation, planning, and resource management.
Ages: 10+ years
Players: 3 to 4 players
Contents: Modular hex tile board, resource cards, building pieces, point markers
Price: $34.75
Available: Yes
--------------
Product:Ticket to Ride
Description: Popular strategy board game in which players collect train cards to claim railway routes between cities and complete secret destination tickets for points. Easy to learn with deep strategic play.
Ages: 8+ years
Players: 2 to 5 players
Contents: Game board (North America map), 225 plastic trains, 110 train cards, 33 destination tickets, longest‑route bonus card, scoring markers, rule booklet  
Price: $44.99
Available: Yes
```

### Example 2

```bash
python3 post_to_app.py -q "What does Ticket to Ride come with?"
```

#### Output

```
OK response:
User ID: user_demo
Answer: Ticket to Ride comes with the following contents:

* Game board (North America map)
* 225 plastic trains
* 110 train cards
* 33 destination tickets
* Longest-route bonus card
* Scoring markers
* Rule booklet
------------------Documents used:-----------------------
Product:Pandemic
Description: Cooperative strategy game where players act as disease‑fighting specialists working together to treat outbreaks and discover cures for four deadly diseases before time runs out. Players either all win or all lose together.
Ages: 8+ years
Players: 2 to 4 players
Contents: World map game board, role cards, pawns, disease cubes, infection cards, player cards, research station pieces, reference cards, rulebook
Price: $49.99
Available: Yes
--------------
Product:Ticket to Ride
Description: Popular strategy board game in which players collect train cards to claim railway routes between cities and complete secret destination tickets for points. Easy to learn with deep strategic play.
Ages: 8+ years
Players: 2 to 5 players
Contents: Game board (North America map), 225 plastic trains, 110 train cards, 33 destination tickets, longest‑route bonus card, scoring markers, rule booklet  
Price: $44.99
Available: Yes
--------------
Product:Catan
Description: Trade and building game set on a resource-rich island. Players collect brick, wood, sheep, wheat, and ore to build settlements, cities, and roads. Involves negotiation, planning, and resource management.
Ages: 10+ years
Players: 3 to 4 players
Contents: Modular hex tile board, resource cards, building pieces, point markers
Price: $34.75
Available: Yes
--------------
Product:Monopoly
Description: Classic game of trade and property building, where players buy, trade houses and hotels, collect rent, and try to bankrupt their opponents. Ideal for long and competitive games.
Ages: 8+ years
Players: 2 to 6 players
Contents: Board, tokens, property cards, houses and hotels, play money, dice
Price: $24.50
Available: Yes
```

### Example 3

```bash
python3 post_to_app.py -q "What's the cost of Monopoly?"
```

#### Output

```
OK response:
User ID: user_demo
Answer: The price of Monopoly is $24.50.
------------------Documents used:-----------------------
Product:Pandemic
Description: Cooperative strategy game where players act as disease‑fighting specialists working together to treat outbreaks and discover cures for four deadly diseases before time runs out. Players either all win or all lose together.
Ages: 8+ years
Players: 2 to 4 players
Contents: World map game board, role cards, pawns, disease cubes, infection cards, player cards, research station pieces, reference cards, rulebook
Price: $49.99
Available: Yes
--------------
Product:Ticket to Ride
Description: Popular strategy board game in which players collect train cards to claim railway routes between cities and complete secret destination tickets for points. Easy to learn with deep strategic play.
Ages: 8+ years
Players: 2 to 5 players
Contents: Game board (North America map), 225 plastic trains, 110 train cards, 33 destination tickets, longest‑route bonus card, scoring markers, rule booklet  
Price: $44.99
Available: Yes
--------------
Product:Monopoly
Description: Classic game of trade and property building, where players buy, trade houses and hotels, collect rent, and try to bankrupt their opponents. Ideal for long and competitive games.
Ages: 8+ years
Players: 2 to 6 players
Contents: Board, tokens, property cards, houses and hotels, play money, dice
Price: $24.50
Available: Yes
--------------
Product:Catan
Description: Trade and building game set on a resource-rich island. Players collect brick, wood, sheep, wheat, and ore to build settlements, cities, and roads. Involves negotiation, planning, and resource management.
Ages: 10+ years
Players: 3 to 4 players
Contents: Modular hex tile board, resource cards, building pieces, point markers
Price: $34.75
Available: Yes
```

## API Endpoint

- **POST** `/query`
  - **Payload:**
    ```json
    {
      "user_id": "user_demo",
      "query": "Your question here"
    }
    ```
  - **Response:**
    ```json
    {
      "user_id": "user_demo",
      "answer": "Response from the bot",
      "docs_used": [...]
    }
    ```

## Running Tests

To run tests (inside Docker):

```bash
docker compose run rag-test
```

Or locally:

```bash
pytest -v --tb=short
```

Alternatively, the `docker compose up --build` command that creates and executes the main service runs a test automatically on startup. If you want to disable this feature, comment out the `rag-test` service in `docker-compose.yml`