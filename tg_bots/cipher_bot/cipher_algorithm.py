'''A primitive password generator tool for SkillFactory webinar 2023.03.01
Features:
choice of password length (with type checking),
the ability for the user to exclude unwanted characters,
the ability to create multiple passwords.
Author: Valery Tropin, tropin.tropin@gmail.com
'''

import random
import string
import time


def get_password_length() -> int:
    while True:
        password_length = input(
            'Введите желаемую длину вашего пароля цифрами:\n'
        )
        if password_length.isdecimal():
            return int(password_length)
        else:
            time.sleep(1)
            print('Пожалуйста, используйте арабские цифры!')
            time.sleep(1)


def get_chars() -> str:
    chars = string.printable.strip()
    print(f'Ваш пароль будет сгенерирован из этого набора символов:\n{chars}')
    time.sleep(1)
    print('Введите символы, которые не хотите использовать (без пробелов)')
    time.sleep(0.5)
    excluded_chars = input('или нажмите Enter, чтобы продолжить без изменений:\n')
    if excluded_chars:
        return ''.join([x for x in chars if x not in excluded_chars])
    else:
        return chars
    

def create_password() -> None:
    while True:
        password_length = get_password_length()
        time.sleep(1)
        password_chars = get_chars()
        time.sleep(1)
        password = ''.join(random.sample(password_chars, password_length))
        print(f'Ваш пароль:\n{password}\n')
        time.sleep(1)
        is_new_password = input(
            'Введите "y" или "д", чтобы создать ещё один пароль или "n" или "н" для отмены\n'
        )
        if is_new_password in ('Y', 'y', 'Д', 'д'):
            create_password()
        else:
            break


create_password()
