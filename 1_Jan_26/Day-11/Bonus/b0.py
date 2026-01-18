def get_average():
    with open("1_Jan_26/Day-11/File/data.txt") as file:
        data = file.readlines()
    values = data[1:]
    values = [float(i) for i in values]

    avg = sum(values) / len(values)
    return avg
    


average = get_average()
print(average)