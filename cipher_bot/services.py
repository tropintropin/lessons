import random
import string


def get_password_length(password_length=None) -> int:
    default_length = 8
    if password_length and password_length.isdecimal():
        return int(password_length)
    return default_length


def get_chars(user_chars=None) -> str:
    chars = string.printable.strip()
    if user_chars:
        return user_chars
    return chars


def create_password(user_settings=None) -> str:
    if user_settings:
        length, chars = user_settings
        password_length = get_password_length(length)
        password_chars = get_chars(chars)
    else:
        password_length = get_password_length()
        password_chars = get_chars()
    if password_length > len(password_chars):
        password_chars = password_chars * password_length
    password = ''.join(random.sample(password_chars, password_length))
    return password

print(string.printable)