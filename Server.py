import socket

# Initialize the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "127.0.0.1"
port = 14200
buffer_size = 1024
server_socket.bind((host, port))  # Replace 'localhost' with your IP
server_socket.listen()
print(f"Server at {host}:{port} listening")
# Initialize bank account balance
balance = 100
client_socket, addr = server_socket.accept()
print(f"Connection from {addr}")


def deposit(amt):
    global balance
    return f"Deposited ${amt}. Current balance: ${balance}"


def withdraw(amt):
    global balance
    if amount > balance:
        return "Insufficient funds"
    else:
        return f"Withdrew ${amt}. Current balance: ${balance}"


def check_balance():
    global balance
    return f"Current balance: ${balance}"


while True:
    # Accept incoming connections

    # Receive client request
    data = client_socket.recv(1024).decode()

    # Process client request and send response
    if data.startswith("DEPOSIT"):
        amount = int(data.split()[1])
        if amount > balance:
            response = "Insufficient funds"
        else:
            balance += amount
            response = deposit(amount)
    elif data.startswith("WITHDRAW"):
        amount = int(data.split()[1])
        balance -= amount
        response = withdraw(amount)
    elif data == "BALANCE":
        response = check_balance()
    else:
        response = "Invalid request"

    client_socket.send(response.encode())

    # Close connection
client_socket.close()
server_socket.close()
