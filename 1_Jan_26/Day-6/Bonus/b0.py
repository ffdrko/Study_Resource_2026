contents = ["All carrots are to be sliced longitudinally.", "The carrots were reportedly sliced.", "All the carrots in the basket are fresh."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"1_Jan_26/Day-6/File/{filename}", "w")
    file.write(content)