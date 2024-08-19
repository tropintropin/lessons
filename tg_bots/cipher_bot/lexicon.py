import string


LEXICON: dict[str, str] = {
    '/start': 'Привет!\n'
                'Этот бот умеет генерировать пароли.\n'
                'Нажмите /help, чтобы посмотреть все доступные команды.',
    '/help': 'Вам доступно два действия:\n1) создать пароль по умолчанию '
                '(длина 8 символов, включает латинские строчные и прописные '
                'буквы, арабские цифры и специальные символы) или\n'
                '2) настроить собственный пароль.',
    'create_password': 'Создать пароль',
    'create_castom': 'Настроить пароль',
    'cancel': 'ОТМЕНИТЬ',
    'user_settings': 'Выберите нужные опции',
}

LEXICON_COMMANDS: dict[str, str] = {
    '/help': 'Помощь',
}

LEXICON_POLL: dict[str, str] = {
    'low_chars': 'прописные буквы',
    'upper_chars': 'строчные буквы',
    'digits_chars': 'цифры',
    'symbols_chars': 'знаки пунктуации',
    'all_chars': 'все символы'
}

# LEXICON_POLL: dict[str, str] = {
#     'low_chars': string.ascii_lowercase,
#     'upper_chars': string.ascii_uppercase,
#     'digits_chars': string.digits,
#     'symbols_chars': string.punctuation,
#     'all_chars': string.printable
# }

