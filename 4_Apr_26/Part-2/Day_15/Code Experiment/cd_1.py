# Experiment - 2 using csv

import csv

with open("File/weather.csv", "r") as file:
    reader = list(csv.reader(file))

# print(reader)   
# print(reader[0][0])
# print(reader[1])
city = input("Enter the city name: ")

for row in reader:
    if row[0].lower() == city.lower():
        print(row[1])