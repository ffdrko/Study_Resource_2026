countries = ["Albania", "Belgium", "Canada", "Denmark", "Estonia", "France"]

for country in countries:
    file = open(f"1_Jan_26/Day-6/File/{country}.txt", "w")
    file.write(country)