import socket

# Set up client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))  # Replace 'localhost' with server IP

while True:
    # User input for command
    command = input("Enter command (DEPOSIT/WITHDRAW/BALANCE): ")

    # Send command to server
    client_socket.send(command.encode('utf-8'))

    # Receive and print server response
    response = client_socket.recv(1024).decode('utf-8')
    print(response)

client_socket.close()
