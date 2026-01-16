countries = ["Albania", "Belgium", "Canada", "Denmark", "Estonia", "France"]
filenames = ["a.txt", "b.txt", "c.txt", "d.txt", "e.txt", "f.txt"]

for country, filename in zip(countries, filenames):
    file = open(f"1_Jan_26/Day-6/File/{filename}", "w")
    file.write(country)