# class Account:
#     def __init__(self, account_number, password):
#         self.account_number = account_number
#         self.__password = password

#     def reset_pass(self, new_password):
#         self.__password = new_password

# acc1 = Account("123", "pass123")

# print(acc1.account_number)
# print(acc1.__password)


class Person:
    def __init__(self, name):
        self.name = name

    def __hello(self):
        print(f"Hello, {self.name}")

    def welcome(self):
        self.__hello()

p1 = Person("Alice")
print(p1.name)
p1.welcome()