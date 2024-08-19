"""
A simple Telegram bot for Hexlet's practice.
"""

import json
import random

# from telegram.ext import Updater, CommandHandler, MessageHandler
# from telegram.ext import Filters
# from telegram import ReplyKeyboardMarkup


# updater = Updater(token='TOKEN', use_context=True)

def is_proper_input(type_=None, min_=None, max_=None):
    while True:
        value_ = input('Enter your answer here: ')
        if type_ is not None:
            try:
                value_ = type_(value_)
            except ValueError:
                print("Input type must be {0}.".format(type_.__name__))
                continue
        if max_ is not None and value_ > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ is not None and value_ < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        else:
            return value_


def translation_direction():
    print("Choose the direction of translation.\nEnter 1 for Russian to English and 2 for English to Russian.")
    direction = is_proper_input(type_=int, min_=1, max_=2)
    return direction


def dict_open():
    with open('cards.json', encoding='utf-8') as cards_file:
        cards = json.load(cards_file)
        return cards


def theme_decision(cards, direction):
    print("Tell me what theme do you want to repeat?\nGreetings - enter 1. Hotel - enter 2.")
    theme_choice = is_proper_input(type_=int, min_=1, max_=2)

    if theme_choice == 1:
        for words in cards["en_ru_greetings"]:
            if direction == 2:
                words = {v: k for k, v in words.items()}
            return words
    elif theme_choice == 2:
        for words in cards["en_ru_hotel"]:
            if direction == 2:
                words = {v: k for k, v in words.items()}
            return words


def level_decision():
    print("Choose the level of difficulty.\nEnter 1 for easy and 2 for hard.")
    level_choice = is_proper_input(type_=int, min_=1, max_=2)

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

        user_answer = is_proper_input(type_=int)

        if user_answer == correct_answer:
            print("Correct!")
            counter -= 1
        else:
            print(f"You failed! Correct answer was '{words[question]}'")
            break

    if not counter:
        print("Congratulations! You did it!")


game(theme_decision(dict_open(), translation_direction()), level_decision())
