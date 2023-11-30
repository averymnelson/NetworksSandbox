# Avery Nelson
# 010920903
# CN CSCE 4753 HW

import socket

PORT = 14200
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(('localhost', PORT))  # Replace 'localhost' with your server IP if needed

while True: 
    #command = input("Enter command (balance/withdraw/deposit): ")
    print("Options:\nDeposit\nWithdraw\nBalance\nQuit")

    choice = input("Enter your selection: ")

    if choice == "Deposit":
        amount = int(input("Enter the deposit amount in whole dollars: "))
        command = f"deposit {amount}"
    elif choice == "Withdraw":
        amount = int(input("Enter the withdrawal amount in whole dollars: "))
        command = f"withdraw {amount}"
    elif choice == "Balance":
        command = "check_balance"
    elif choice == "Quit":
        print("Exiting the program. Goodbye.")
        break
    else:
        print("Invalid choice. Please try again.")
        continue
    
    clientSocket.send(command.encode('utf-8'))
    response = clientSocket.recv(1024).decode('utf-8')
    print(response)
    print("\n\n")

clientSocket.close()