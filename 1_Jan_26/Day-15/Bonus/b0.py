import json

count = 0
ques = 0

with open('questions.json') as f:
    content = f.read()

data = json.loads(content)

for question in data:
    print(question['question_text'])
    for index, alternative in enumerate(question['alternative']):
        print(f'{index + 1}-{alternative}')
    user_choice = int(input("Enter your choice: "))
    question['user_choice'] = user_choice
    if question['user_choice'] == question['correct_answer']:
        count += 1
        ques += 1
        print(f'your score is: {count}/{ques}')
    else:
        ques += 1
        print(f"The correct answer is {question['correct_answer']}")
        print(f'your score is: {count}/{ques}')


print(f'Your have answer correctly: {count}/{ques}')