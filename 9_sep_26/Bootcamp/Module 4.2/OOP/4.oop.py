class Bank:
    def __init__(self, balance, account_number):
        self.balance = balance
        self.account_number = account_number

    def debit(self, amount):
        if amount <= self.balance and self.balance > 0:
            self.balance -= amount
            print(f"Debited {amount}. New balance is {self.balance}")

    def credit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Credited {amount}. New balance is {self.balance}")


    def get_balance(self):
        print(f"Current balance is {self.balance}")

user_1 = Bank(1000, "1111")
user_1.debit(200)
user_1.credit(500)
user_1.get_balance()