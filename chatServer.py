import socket                           # socket library for network communication
import threading                        # to handle multiple clients simultaneously


# host = socket.gethostbyname(socket.gethostname())
host = "127.0.0.1"                      # Localhost address for testing
port = 55555                            # Port number where the server will listen for connections

# Create a socket object for the server
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,port))                # Bind the server to the specified host and port
server.listen()                         # Set the server to listen for incoming connections

# Lists to store connected clients and their nicknames
clients = []
nicknames = []

# Function to broadcast a message to all connected clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle communication with a single client
def handle(client):
    while True:
        try:
            message = client.recv(1024)                 # Receive a message from the client
            broadcast(message)
        except:
            # Handle client disconnection
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            # Notify other clients that this client has left the chat
            broadcast(f"{nickname} has left the chat!".encode('utf-8'))
            print(f"{nickname} has left the chat!")
            nicknames.remove(nickname)
            break

# Function to handle incoming connections and assign nicknames
def receive():
    while True:
        # Accept a new client connection
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        # Request the client's nickname
        client.send("nickname".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')

        # Store the new client and their nickname
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname of the client is {nickname}")
        # Notify all clients that a new user has joined
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send("Connected to the server".encode('utf-8'))

        # Start a new thread to handle this client's communication
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()


if __name__ == '__main__':
    print("Server is listening")
    receive()                                   # Start accepting connections
