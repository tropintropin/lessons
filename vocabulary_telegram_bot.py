'''
A simple Telegram bot for Hexlet's practice.
'''

from itertools import count
import random

# '': '',
en_ru_greetings = {
    'здравствуйте': 'hello',
    'привет': 'hi',
    'добрый вечер': 'good evening',
    'добрый день': 'good day',
    'доброе утро': 'good morning',
    'доброй ночи': 'good night',
    'до свидания': 'good bye',
    'пока': 'bye',
    'до встречи': 'see you'
}

en_ru_hotel = {
    'гостиница, отель': 'hotel',
    'номер на одного': 'single room',
    'номер на двоих': 'double room',
    'Я бы хотел заказать номер': 'I want to order a room',
    'У вас есть свободные номера?': 'Do you have a room?',
    '': '',
    '': '',
    '': '',
    '': ''
}

print('Tell me what theme do you want to repeat?')
print('Greetings - enter 1. Hotel - enter 2.')
theme_choice = int(input('Enter your choice here: '))
if theme_choice == 1:
    words = en_ru_greetings
elif theme_choice == 2:
    words = en_ru_hotel

level_choice = int(input('Choose the level of difficulty: enter 1 for easy and 2 for hard.'))
if level_choice == 1:
    level = 4
elif level_choice == 2:
    level = 9

counter = 5
while counter:
    answers = random.sample(list(words.keys()), level)
    question = random.choice(answers)

    print(f'Which word matches "{question}"?')

    correct_answer = 0
    for i, answer in enumerate(answers, start=1):
        if answer == question:
            correct_answer = i

        print(i, words[answer])
    
    user_answer = int(input('Enter the correct number: '))

    if user_answer == correct_answer:
        print('Correct!')
        counter -= 1
    else:
        print(f'You failed! Correct answer was "{words[question]}"')
        break

if not counter:
    print('Congratulations! You did it!')