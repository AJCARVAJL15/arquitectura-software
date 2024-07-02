import socket
import threading

host='localhost'
port=55555

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((host, port))
serversocket.listen()
print(f"Server running on {host}:{port}")

clients=[]
usernames=[]

def broadcast(message,_client):
    for client in clients:
        if client != _client:
            client.send(message)
        

def handle_messages(client):
    while True:
        try:
            message=client.recv(1024)
            broadcast(message,client)
        except:
            index=client.index(client)
            username=usernames[index]
            broadcast(f"Chatbot: {username} Desconectado".encode('utf-8'))
            clients.remove(client)
            usernames.remove(username)
            client.close()
            break


def receive_connections():
    while True:
        client,addres= serversocket.accept()

        client.send("@username".encode('utf-8'))
        username=client.recv(1024).decode('utf-8')

        clients.append(client)
        usernames.append(username)

        print(f"{username} est conectado en la direccion {str(addres)}")

        message=f"ChatBot: {username} se ha unido al chat".encode("utf-8")
        broadcast(message,client)
        client.send("Conectado al servidor".encode("utf-8"))

        thread=threading.Thread(target=handle_messages,args=(client,))
        thread.start()

    
receive_connections()
