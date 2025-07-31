import requests

response = requests.post(
    "http://localhost:8000/query",
    json={
        "user_id": "user123",
        "query": "¿Cuál es el producto más barato que tienen?"
    }
)

print("Status:", response.status_code)
print("Response:", response.json())
