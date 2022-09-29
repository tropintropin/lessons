"""
A simple Telegram bot for Hexlet's practice.
"""

import json
import random

# from telegram.ext import Updater, CommandHandler, MessageHandler
# from telegram.ext import Filters
# from telegram import ReplyKeyboardMarkup


# updater = Updater(token='TOKEN', use_context=True)


def translation_direction():
    while True:
        direction = int(input("Choose the direction of translation.\nEnter 1 for Russian to English and 2 for English to Russian: "))
        if not direction.isnumeric() and (direction != 1 or direction != 2):
            print('Please enter 1 or 2: ')
            continue
        else:
            break
    return direction


def dict_open():
    with open('cards.json', encoding='utf-8') as cards_file:
        cards = json.load(cards_file)
        return cards


def theme_decision(cards, direction):
    print("Tell me what theme do you want to repeat?\nGreetings - enter 1. Hotel - enter 2.")
    while True:
        theme_choice = int(input("Enter your choice here: "))
        if not theme_choice.isnumeric() and (theme_choice != 1 or theme_choice != 2):
            print('Please enter 1 or 2: ')
            continue
        else:
            break

    if theme_choice == 1:
        for words in cards["en_ru_greetings"]:
            # обратный словарь сюда
            if direction == 2:
                words = {v: k for k, v in words.items()}
            return words
    elif theme_choice == 2:
        for words in cards["en_ru_hotel"]:
            # обратный словарь сюда
            if direction == 2:
                words = {v: k for k, v in words.items()}
            return words


def level_decision():
    while True:
        level_choice = int(input("Choose the level of difficulty.\nEnter 1 for easy and 2 for hard: "))
        if not level_choice.isnumeric() and (level_choice != 1 or level_choice != 2):
            print('Please enter 1 or 2: ')
            continue
        else:
            break

    if level_choice == 1:
        level = 4
    elif level_choice == 2:
        level = 9
    return level


def game(words, level):
    counter = 5
    while counter:
        answers = random.sample(list(words.keys()), level)
        question = random.choice(answers)

        print(f"Which word matches '{question}'?")

        correct_answer = 0
        for i, answer in enumerate(answers, start=1):
            if answer == question:
                correct_answer = i

            print(i, words[answer])

        while True:
            user_answer = int(input("Enter the correct number: "))
            if not user_answer.isnumeric():
                print('Please enter a number: ')
                continue
            else:
                break

        if user_answer == correct_answer:
            print("Correct!")
            counter -= 1
        else:
            print(f"You failed! Correct answer was '{words[question]}'")
            break

    if not counter:
        print("Congratulations! You did it!")


game(theme_decision(dict_open(), translation_direction()), level_decision())
