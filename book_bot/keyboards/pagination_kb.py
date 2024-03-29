# https://stepik.org/lesson/759408/step/12?unit=761424

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from lexicon.lexicon import LEXICON


# Функция, генерирующая клавиатуру для страницы книги
def create_pagination_keyboard(*buttons: str) -> InlineKeyboardMarkup:
    # Создаем объект клавиатуры
    pagination_kb: InlineKeyboardMarkup = InlineKeyboardMarkup()
    # Наполняем клавиатуру кнопками
    pagination_kb.row(*[InlineKeyboardButton(
        LEXICON[button] if button in LEXICON else button,
        callback_data=button) for button in buttons])
    return pagination_kb
