filenames = ['a.txt', 'b.txt', 'c.txt']

for file in filenames:
    files = open(f'File/{file}', 'r')
    print(files.read())