contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reportedly sliced",
            "The slicing process was well present"]

file = ["doc.txt", 'report.txt', 'presentation.txt']

for content, filename in zip(contents, file):
    files = open(f"{filename}", "w")
    files.write(content)
    files.close()