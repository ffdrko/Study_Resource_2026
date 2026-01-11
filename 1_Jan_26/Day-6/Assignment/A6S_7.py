member = input("Add a new member: ")


file = open("1_Jan_26/Day-6/File/members.txt", "r")
member_name = file.readlines()


file = open("1_Jan_26/Day-6/File/members.txt", "w")
file.writelines(member + "\n")