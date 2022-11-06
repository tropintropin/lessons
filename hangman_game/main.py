import json
import random
from stages import stages


def get_word() -> str:
    with open('words.json', 'r', encoding='utf-8') as f:
        word_list = json.load(f)
    return random.choice(word_list).upper()


def display_hangman(tries: int) -> str:
    if 0 <= tries <= 6:
        return stages[tries]
