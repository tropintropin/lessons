"""
A simple Telegram bot for Hexlet's practice.
"""

import json
import random


def translation_direction():
    direction = int(input("Choose the direction of translation.\nEnter 1 for Russian to English and 2 for English to Russian: "))
    return direction


def dict_open():
    with open('cards.json', encoding='utf-8') as cards_file:
        cards = json.load(cards_file)
        return cards


def theme_decision(cards, direction):
    print("Tell me what theme do you want to repeat?\nGreetings - enter 1. Hotel - enter 2.")
    theme_choice = int(input("Enter your choice here: "))
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
    level_choice = int(input("Choose the level of difficulty.\nEnter 1 for easy and 2 for hard: "))
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

        user_answer = int(input("Enter the correct number: "))

        if user_answer == correct_answer:
            print("Correct!")
            counter -= 1
        else:
            print(f"You failed! Correct answer was '{words[question]}'")
            break

    if not counter:
        print("Congratulations! You did it!")


game(theme_decision(dict_open(), translation_direction()), level_decision())
