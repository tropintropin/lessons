'''A primitive password generator Telegram bot
for SkillFactory webinars 2023.03.01—03
Features:
choice of password length (with type checking),
the ability for the user to exclude unwanted characters,
the ability to create multiple passwords.
Author: Valery Tropin, tropin.tropin@gmail.com
'''

import random
import string

from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from config import BOT_TOKEN


bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher()


async def process_start_command(message: Message):
    await message.answer('Введите желаемую длину вашего пароля цифрами:\n')


async def process_get_password(message: Message):
    password_length = message.text
    try:
        if 74 < int(password_length) < 0:
            await message.reply('Недопустимый размер пароля')
        else:
            password = ''.join(random.sample(string.printable, 8))
            await message.answer(f'Ваш пароль: {password}')
    except Exception as ex2:
        await message.answer('Необходимо ввести число от 1 до 74')


dp.message.register(CommandStart(), process_start_command)
dp.message.register(Command(commands='get_password'), process_get_password)


if __name__ == '__main__':
    dp.run_polling(bot)
