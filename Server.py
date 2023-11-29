import socket

# Initialize the balance
balance = 100.0

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", 8888))  # Replace 'localhost' with your server IP if needed
server_socket.listen(1)

print("Server started. Waiting for a connection...")

while True:
    # Accept incoming connections
    client_socket, addr = server_socket.accept()
    print("Connection from", addr)

    while True:
        data = client_socket.recv(1024).decode()

        if not data:
            break

        # Process client requests
        if data == 'check_balance':
            client_socket.send(str(balance).encode())
        elif data.startswith('withdraw'):
            amount = float(data.split(' ')[1])
            if balance >= amount:
                balance -= amount
                client_socket.send("Withdrawal successful".encode())
            else:
                client_socket.send("Insufficient funds".encode())
        elif data.startswith('deposit'):
            amount = float(data.split(' ')[1])
            balance += amount
            client_socket.send("Deposit successful".encode())

    client_socket.close()
