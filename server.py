import socket
import threading
import random

# Diffie-Hellman parameters
p = 23  # A prime number
g = 5   # A primitive root modulo p

def handle_client(client_socket):
    # Server's private key
    b = random.randint(1, p-1)
    B = pow(g, b, p)
    
    # Receive client's public key
    A = int(client_socket.recv(1024).decode())
    
    # Send server's public key
    client_socket.send(str(B).encode())

    
    # Compute shared secret
    shared_secret = pow(A, b, p)
    print(f"Shared secret: {shared_secret}")
    
    client_socket.close()


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("Server listening on port 9999")
    
    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
