# Avery Nelson
# 010920903
# CN CSCE 4753 HW

import socket

# Initialize the balance
balance = 100
PORT = 14200
# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("127.0.0.1", PORT))  # Replace 'localhost' with your server IP if needed
server_socket.listen(1)
print(f"Server listening on 127.0.0.1:{PORT}. Waiting for a connection...")
client_socket, addr = server_socket.accept()
print("Connection from", addr)
    # Accept incoming connections
def deposit(amount):
    global balance
    if amount < 0:
        return "Invalid amount attempted. You cannot deposit a negative amount."
    balance += amount
    return f"Deposited {amount} successfully. \n{check_balance()}"

def withdraw(amount):
    global balance
    if amount > balance:
        return "Insufficient funds"
    elif amount < 0:
        return "Invalid amount attempted. You cannot withdraw a negative amount."
    balance -= amount
    return f"Withdrawn {amount} successfully. \n{check_balance()}"

def check_balance():
    return f"Current balance: ${balance}"

while True:
    data = client_socket.recv(1024).decode()

    if not data:
        break

    # Process client requests
    if data == 'check_balance':
        response = check_balance()
        client_socket.send(response.encode())
    elif data.startswith('withdraw'):
        amount = float(data.split(' ')[1])
        response = withdraw(amount)
        client_socket.send(response.encode())
    elif data.startswith('deposit'):
        amount = float(data.split(' ')[1])
        response = deposit(amount)
        client_socket.send(response.encode())

client_socket.close()
