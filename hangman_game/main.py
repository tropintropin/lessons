import json
import random


def get_word() -> str:
    with open('words.json', 'r', encoding='utf-8') as f:
        word_list = json.load(f)
    return random.choice(word_list).upper()


print(get_word())
