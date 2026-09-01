user_id = ["001", "002", "003"]
user_names = ["Alvi", "Sadia", "Abir"]
user_mails = ["alvi@mail.com", "sadia@gmail.com", "abir@yahoo.com"]
user_age = [22, 20, 21]


for idx in range(len(user_id)):
    print(idx)


for user_id, user_name, user_mail, user_age in zip(user_id, user_names, user_mails, user_age):
    print(f"{user_id}-{user_name}-{user_mail}-{user_age}")