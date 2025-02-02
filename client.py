import socket
import random

# Diffie-Hellman parameters
p = 23  # A prime number
g = 5   # A primitive root modulo p

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("127.0.0.1", 9999))
    
    # Client's private key
    a = random.randint(1, p-1)
    A = pow(g, a, p)
    
    # Send client's public key
    client.send(str(A).encode())
    
    # Receive server's public key
    B = int(client.recv(1024).decode())
    
    # Compute shared secret
    shared_secret = pow(B, a, p)
    print(f"Shared secret: {shared_secret}")
    
    client.close()

if __name__ == "__main__":
    start_client()
