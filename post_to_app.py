import requests

url = "http://localhost:8000/query"
payload = {
    "user_id": "usuario_demo",
    "query": "¿Qué juegos están disponibles en tienda?"
}

response = requests.post(url, json=payload)
if response.ok:
    print("Respuesta de la app:")
    print(response.json())
else:
    print(f"Error {response.status_code}: {response.text}")
