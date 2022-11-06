'''
Hangman is a linguistic game in which you have to guess the word \
    and prevent the little man from being hanged.
'''


import json
import random
from stages import display_hangman


def get_letter() -> str:
    while True:
        letter = input('Введите букву: ').upper()
        if len(letter) == 1 and 1039 < ord(letter) < 1072:
            return letter


def get_word() -> str:
    with open('words.json', 'r', encoding='utf-8') as f:
        word_list = json.load(f)
    return random.choice(word_list).upper()


def print_words(word_completion):
    print('~ ' * len(word_completion))
    print(*word_completion, sep=' ')


def play():
    guessed_words = []
    guessed = False
    ask_word = [x for x in get_word()]
    word_completion = ['_' for _ in range(len(ask_word))]
    guessed_letters = []
    tries = 6

    print('Сыграем в «Висельника»!')
    print('Вам нужно отгадать слово:')
    print_words(word_completion)
    print('Вам дано 6 попыток. За каждый неверный ответ висельник\n \
        приблизится к эшафоту!')
    print(display_hangman(tries))

    while tries:
        if ''.join(ask_word) == ''.join(word_completion):
            guessed_words.append(''.join(ask_word))
            print('Ты победил! Загаданное слово было:')
            print_words(ask_word)
            guessed = True
            break

        user_guess = get_letter()
        if user_guess in guessed_letters:
            print('Эта буква уже была! Давай другую.')
            user_guess = get_letter()

        if user_guess in ask_word:
            guessed_letters.append(user_guess)
            for i, v in enumerate(ask_word):
                if user_guess == v:
                    word_completion[i] = user_guess
            print('Так держать!')
            print_words(word_completion)
        else:
            guessed_letters.append(user_guess)
            tries -= 1
            print_words(word_completion)
            print(f'Неверно! Осталось {tries} попыток!')
            print(display_hangman(tries))
    if not guessed:
        print_words(word_completion)
        print('Ты проиграл и не спас своего висельника!')
        print('Загаданное слово было:')
        print_words(ask_word)
    return guessed_words


def game():
    guessed_words = []
    while True:
        guessed_words.append(play())
        if guessed_words:
            print('Угаданные слова:')
            print(*guessed_words, sep=' ')
        print('Хотите сыграть ещё? "Д" — да, "Н" — нет.')
        ask = get_letter()
        if ask == 'Д':
            guessed_words.append(play())
        else:
            break


game()
