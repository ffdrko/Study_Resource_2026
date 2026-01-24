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

for index, question in enumerate(data):
    if question['user_choice'] == question['correct_answer']:
        count += 1
        result = 'Correct answer'
    else:
        result = 'Incorrect answer'

    message = (f"{index + 1} {result} -Your answer: {question['user_choice']}  "
               f"correct answer: {question['correct_answer']}")

    print(message)
