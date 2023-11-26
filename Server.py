import socket

# Initialize the server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 12345))  # Replace 'localhost' with your IP
server_socket.listen(1)

# Initialize bank account balance
balance = 100

def deposit(amount):
    global balance
    balance += amount
    return f"Deposited ${amount}. Current balance: ${balance}"

def withdraw(amount):
    global balance
    if amount > balance:
        return "Insufficient funds"
    else:
        balance -= amount
        return f"Withdrew ${amount}. Current balance: ${balance}"

def check_balance():
    global balance
    return f"Current balance: ${balance}"

while True:
    # Accept incoming connections
    client_socket, addr = server_socket.accept()
    print(f"Connection from {addr}")

    # Receive client request
    request = client_socket.recv(1024).decode()

    # Process client request and send response
    if request.startswith("DEPOSIT"):
        amount = float(input("Enter deposit amount: "))
        response = deposit(amount)
    elif request.startswith("WITHDRAW"):
        amount = float(input("Enter withdrawal amount: "))
        response = withdraw(amount)
    elif request == "BALANCE":
        response = check_balance()
    else:
        response = "Invalid request"

    client_socket.send(response.encode())

    # Close connection
    client_socket.close()
