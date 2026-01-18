def format_filename():
    filename = "report.txt"
    alter_file = filename.replace(".txt", "").capitalize()
    return alter_file


print(format_filename())
print(len(format_filename()))