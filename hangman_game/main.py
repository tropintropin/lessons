import json
import random
from stages import display_hangman


def get_letter() -> str:
    while True:
        letter = input('Введите букву: ').upper()
        if 1039 < ord(letter) < 1072:  # Only cirillic upper letters
            return letter


def get_word() -> str:
    with open('words.json', 'r', encoding='utf-8') as f:
        word_list = json.load(f)
    return random.choice(word_list).upper()


# def play(word: str):
#     word_completion = '_' * len(word)
#     guessed = False
#     guessed_letters = []
#     guessed_words = []
#     tries = 6
