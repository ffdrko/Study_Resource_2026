import csv

with open('../file/weather.csv') as file:
    date = list(csv.reader(file))

city = input("Enter City: ")

for row in date[1:]:
    if row[0] == city:
        print(row[1])