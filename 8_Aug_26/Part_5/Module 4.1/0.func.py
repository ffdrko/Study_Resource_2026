def greet():
    print("From the inside.")


greet()


def greet_1(name):
    print(f"Hello, {name}")
    print(f"How are you, {name}")


employ_list = ["Fahim", "Faisal", "Deepto"]

for i in employ_list:
    greet_1(i)