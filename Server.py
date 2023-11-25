import socket
import sys


def main():
    host = socket.gethostname()
    port = 12200
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    c, addr = s.accept()
    print('Got connection from', addr)
    account = Server()
    while True:
        userchoice = c.recv(1024).decode()
        if userchoice == b'1':
            c.send("How much would you like to deposit today?".encode())
            amount = float(c.recv(1024).decode())
            account.deposit(amount, c)
        elif userchoice == b'2':
            c.send("How much would you like to withdraw?".encode())
            amount = float(c.recv(1024).decode())
            account.withdrawal(amount, c)
        elif userchoice == b'3':
            account.print_balance(c)
        elif userchoice == b'4':
            c.send("Thank you for banking with us!".encode())
            sys.exit(1)
        else:
            print("Wrong Choice!")
            c.send("Wrong Choice!".encode())

        c.close()  # Close the connection


class Server:
    def __init__(self):
        self.account_balance = float(10000)
        self.beginning_balance = self.account_balance
        self.deposit_amount = float(0)
        self.withdrawal_amount = float(0)

    def deposit(self, amount, conn):
        self.account_balance += amount
        self.deposit_amount += amount
        print("Deposit was $%.2f, current balance is $%.2f" % (amount, self.account_balance))
        data = "Deposit was $%.2f, current balance is $%.2f" % (amount, self.account_balance)
        conn.send(data.encode())

    def withdrawal(self, amount, conn):
        self.account_balance -= amount
        self.withdrawal_amount += amount
        print("Withdrawal was $%.2f, current balance is $%.2f" % (amount, self.account_balance))
        data = "Withdrawal was $%.2f, current balance is $%.2f" % (amount, self.account_balance)
        conn.send(data.encode())

    def print_balance(self, conn):
        print("Your current balance: $%.2f" % self.account_balance)
        data = "Your current balance: $%.2f" % self.account_balance
        conn.send(data.encode())

    main()
