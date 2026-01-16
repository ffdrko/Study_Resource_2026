temperature = [10, 12, 14]

file = open("1_Jan_26/Day-7/File/tem.txt", "w")
file.writelines(str(temperature) + '\n' for temperature in temperature)