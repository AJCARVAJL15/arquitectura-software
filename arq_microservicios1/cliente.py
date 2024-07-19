import requests

# mensajes
response = requests.get('http://localhost:5001/messages')
print(f"mensajes: {response.status_code}, {response.json()}")

# saludos
response = requests.get('http://localhost:5005/greetings')
print(f"saludos: {response.status_code}, {response.json()}")
