file = open("File/name.txt", "r")
name_list = file.readlines()
file.close()

name_list.append("John\n")


file = open("File/name.txt", "w")
file.writelines(name_list)
file.close()

