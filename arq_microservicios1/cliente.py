import requests

# Get messages
response = requests.get('http://localhost:5001/messages')
print(f"Messages: {response.status_code}, {response.json()}")

# Get greetings
response = requests.get('http://localhost:5002/greetings')
print(f"Greetings: {response.status_code}, {response.json()}")

