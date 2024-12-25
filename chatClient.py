import socket
import threading



# Function to handle receiving messages from the server
def receive():
    while True:
        try:
            # Receive a message from the server
            message = client.recv(1024).decode('utf-8')
            if message == 'nickname':
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            # Handle any errors, such as server disconnection
            print("Error occurred")
            client.close()
            break

# Function to handle sending messages to the server
def write():
    while True:
        # Format the message with the user's nickname and input
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))



if __name__ == '__main__':
    # Prompt the user to choose a nickname
    nickname = input("Choose a nickname: ")

    # Create a socket object for the client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 55555))  # Connect the client to the server's host and port

    # Start a thread for receiving messages
    receive_thread = threading.Thread(target=receive)
    receive_thread.start()

    # Start a thread for sending messages
    write_thread = threading.Thread(target=write)
    write_thread.start()