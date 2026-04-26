# Experiment - 2 using csv

import csv

with open("File/weather.csv", "r") as file:
    reader = list(csv.reader(file))
    
city = input("Enter the city name: ")

for row in reader:
    if row[0].lower() == city.lower():
        print(row[1])