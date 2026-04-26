import json

count = 0
with open('Bonus\ques.json', 'r') as f:
    content = f.read()

data = json.loads(content)

for question in data:
    print(question['question_text'])
    for index, option in enumerate(question['alternatives']):
        print(f"{index + 1}. {option}")
    answer = int(input('Your answer: ')) - 1
    question["user_answer"] = answer
    if question["user_answer"] == question['correct_answer']:
        print('Correct!')
        count += 1
    else:
        print(f'Wrong! The correct answer is: {question["correct_answer"]}')

print(f'Your final score is: {count}/{len(data)}')