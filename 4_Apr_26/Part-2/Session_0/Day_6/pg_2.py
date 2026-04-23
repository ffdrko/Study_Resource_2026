filenames = ['doc_1.txt', 'report_1.txt', 'presentation_1.txt']

for file in filenames:
    files = open(f"File/{file}", "w")
    files.write("Hello")