import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 8888))  # Replace 'localhost' with your server IP if needed

while True:
    print("\n1. Check balance\n2. Deposit money\n3. Withdraw money\n4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        client_socket.send('check_balance'.encode())
        response = client_socket.recv(1024).decode()
        print("Balance:", response)
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        client_socket.send(f"deposit {amount}".encode())
        print(client_socket.recv(1024).decode())
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        client_socket.send(f"withdraw {amount}".encode())
        print(client_socket.recv(1024).decode())
    elif choice == '4':
        client_socket.close()
        break
    else:
        print("Invalid choice")
