import socket

HOST = "192.168.3.172"
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    
    message = "Hello from client"
    client_socket.sendall(message.encode())

    data = client_socket.recv(1024)
    print(f"Received from server: {data.decode()}")
