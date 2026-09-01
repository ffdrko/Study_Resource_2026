class ATM:
    def __init__(self, balance):
        self.__balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.__balance}")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.__balance}")



atm1 = ATM(1000)

# atm1.check_balance()

atm1.deposit(500)

print(self.__balance)