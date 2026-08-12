#create bankaccount class with accountNumber, Holder Name and balance
#BALANCE Must be modified only from the class
#implementation of deposit and withdraw
#No negative values deposit or withdrawal
#create and perform multiple transactions

class BankAccount:
    def __init__(self):
        self.acc_number = None
        self.holder_name = None
        self.balance = 1000

    def deposit(self, acc, name, amount):
        if amount <= 0:
            print("No negative Values or Zero values could be deposited. Amount should be Above 1 Rupee")
        else:
            self.acc_number = acc
            self.holder_name = name
            self.balance += amount
            print("The amount has been successfully deposited")
    def withdraw(self, acc, name, amount):
        if  self.balance < amount:
            print("Insufficient Balance")
        else:
            self.acc_number = acc
            self.holder_name = name
            self.balance -= ammount
            print("The amount has been Debited")
Bank = BankAccount()
while True:
    print("\n 1. Deposit\n 2. Withdraw\n 3. Exit\n")
    c = int(input("Enter your choice: "))
    if c==1:
        acc=input("Enter the Account Number: ")
        name=input("Enter the Holders Name: ")
        amount=int(input("Enter the amount to be deposited"))
        Bank.deposit(acc,name,amount)
    if c==2:
        acc=input("Enter the Account Number: ")
        name=input("Enter the Holders Name: ")
        amount=int(input("Enter the amount to be Withdrawed"))
        Bank.withdraw(acc,name,amount)
    if c==3:
        break