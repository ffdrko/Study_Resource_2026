# temperatures = [10, 12, 14]

# file = open("file.txt", 'w')

# file.writelines(temperatures)

temperatures = [10, 12, 14]
temp = [str(i) + '\n' for i in temperatures]

file = open("D:\FFD WORK\FFD\Study_Resource_2026/4_Apr_26\Part-2\Day_7\File/temps.txt", "w")
file.writelines(temp)
