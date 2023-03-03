from aiogram import Bot
from aiogram.types import BotCommand, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from lexicon import LEXICON, LEXICON_COMMANDS


def create_passwords_keyboard(*args) -> InlineKeyboardMarkup:
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    kb_builder.row(
        InlineKeyboardButton(
        text=LEXICON['create_password'],
        callback_data='create_password'
        ),
        InlineKeyboardButton(
        text=LEXICON['create_castom'],
        callback_data='create_castom'
        )
    )
    kb_builder.row(
        InlineKeyboardButton(
        text=LEXICON['cancel'],
        callback_data='cancel'
        )
    )
    return kb_builder.as_markup()


async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(
            command=command,
            description=description
        ) for command, description in LEXICON_COMMANDS.items()
    ]
    await bot.set_my_commands(main_menu_commands)
