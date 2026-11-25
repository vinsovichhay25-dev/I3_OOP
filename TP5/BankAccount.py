class BankAccount:
    bank_name = "ITC Bank"

    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance


    def deposit(self, amount):
        if amount <= 0:
            print("Your amount should be positive")
        else:
            print(f"Deposit: ${amount}")
            self.__balance += amount
            print(f"New Balance: ${self.__balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Your amount should be positive")
        elif amount > self.__balance:
            print("Insufficient Fund")
        else:
            print(f"Withdraw: ${amount}")
            self.__balance -= amount
            print(f"Final Balance: ${self.__balance}")

    def display_balance(self):
        print(f"Bank: {self.bank_name}")
        print(f"Account Owner: {self.owner}")
        print(f"Initial Balance: ${self.__balance}")

bank_acc1 = BankAccount("Visal", 101, 1000)
bank_acc2 = BankAccount("Ronan", 102, 3000)

bank_acc1.display_balance()
print(" ")

bank_acc1.deposit(500)
print(" ")

bank_acc1.withdraw(200)
print(" ")
