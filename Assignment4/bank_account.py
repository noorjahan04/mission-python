class BankAccount:
    def __init__(self, account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully:", amount)
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully:", amount)
        else:
            print("Insufficient balance or invalid amount")

    def check_balance(self):
        print("Current Balance:", self.balance)


# Creating an object
account1 = BankAccount(12345, "Noor", 5000)

# Calling methods
print("Account Number:", account1.account_number)
print("Owner Name:", account1.owner_name)

account1.check_balance()
account1.deposit(2000)
account1.withdraw(1000)
account1.check_balance()