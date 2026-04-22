def get_average():
    with open("File/data.txt", "r") as file:
        numbers = file.readlines()[1:]
        num = [float(i.strip()) for i in numbers]
        avg = sum(num) / len(num)
    return avg


average = get_average()
print(average)