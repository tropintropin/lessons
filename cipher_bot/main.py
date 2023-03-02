from aiogram import Bot, types, Dispatcher

from config import BOT_TOKEN

import random
import string


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


async def start_command(message: types.Message):
    await message.answer('Введите желаемую длину вашего пароля цифрами:\n')


async def get_password(message: types.Message):
    password_length = message.text
    try:
        if 74 < password_length < 0:
            await message.reply('Недопустимый размер пароля')
        else:
            password = ''.join(random.sample(string.printable, 8))
            await message.answer(f'Ваш пароль: {password}')
    except Exception as ex2:
        await message.answer('Необходимо ввести число от 1 до 74')


if __name__ == '__main__':
    Dispatcher.start_polling(dp)
