"""A simple Telegram bot for guessing numbers from 1 to 100
https://stepik.org/lesson/759400/step/1?unit=761416
https://stepik.org/lesson/759400/step/2?unit=761416
https://stepik.org/lesson/759400/step/3?unit=761416
https://stepik.org/lesson/759400/step/5?unit=761416
"""

import random

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.dispatcher.filters import Text

from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

users = {}

ATTEMPTS = 5

def get_random_number() -> int:
    return random.randrange(1, 101)


async def process_start_command(message: Message):
    await message.answer('Привет!\nДавай сыграем в игру "Угадай число"?\n\nЧтобы получить правила игры и список доступных команд - отправьте команду /help')

    if message.from_user.id not in users:
        users[message.from_user.id] = {
            'in_game': False,
            'secret_number': None,
            'attempts': None,
            'total_games': 0,
            'wins': 0
        }


async def process_help_command(message: Message):
    await message.answer(f'Правила игры:\n\nЯ загадываю число от 1 до 100, а вам нужно его угадать\nУ вас есть {ATTEMPTS} попыток\n\nДоступные команды:\n/help - правила игры и список команд\n/cancel - выйти из игры\n/stat - посмотреть статистику\n\nДавай сыграем?')


async def process_stat_command(message: Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer('Игра не запущена. Чтобы запустить, введите /start, чтобы узнать о других командах, введите /help')
    await message.answer(f'Всего игр сыграно: {users[message.from_user.id]["total_games"]}\nИгр выиграно: {users[message.from_user.id]["wins"]}')


async def process_cancel_command(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer('Вы вышли из игры. Если захотите сыграть снова — напишите об этом')
        users[message.from_user.id]['in_game'] = False
    else:
        await message.answer('А мы и не играем. Может, сыграем разок?')


async def process_positive_unswer(message: Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer('Ура!\n\nЯ загадал число от 1 до 100, попробуй угадать!')
        users[message.from_user.id]['in_game'] = True
        users[message.from_user.id]['secret_number'] = get_random_number()
        users[message.from_user.id]['attempts'] = ATTEMPTS
    else:
        await message.answer('Пока мы играем в игру я могу реагировать только на числа от 1 до 100 и команды /cancel и /stat')


async def process_negative_command(message: Message):
    if not users[message.from_user.id]['in_game']:
        await message.answer('Жаль :(\n\nЕсли захотите поиграть - просто напишите об этом')
    else:
        await message.answer('Мы же сейчас с вами играем. Присылайте, пожалуйста, числа от 1 до 100')


async def process_numbers_unswer(message: Message):
    if users[message.from_user.id]['in_game']:
        if int(message.text) == users[message.from_user.id]['secret_number']:
            await message.answer('Ура!!! Вы угадали число!\n\nМожет, сыграем еще?')
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
            users[message.from_user.id]['wins'] += 1
        elif int(message.text) > users[message.from_user.id]['secret_number']:
            await message.answer('Мое число меньше')
            users[message.from_user.id]['attempts'] -= 1
        elif int(message.text) < users[message.from_user.id]['secret_number']:
            await message.answer('Мое число больше')
            users[message.from_user.id]['attempts'] -= 1
        
        if users[message.from_user.id]['attempts'] == 0:
            await message.answer(f'К сожалению, у вас больше не осталось попыток. Вы проиграли :(\n\nМое число было {users[message.from_user.id]["secret_number"]}\n\nДавайте сыграем еще?')
            users[message.from_user.id]['in_game'] = False
            users[message.from_user.id]['total_games'] += 1
    else:
        await message.answer('Мы еще не играем. Хотите сыграть?')


async def process_other_text_answers(message: Message):
    if users[message.from_user.id]['in_game']:
        await message.answer('Мы же сейчас с вами играем. Присылайте, пожалуйста, числа от 1 до 100')
    else:
        await message.answer('Я довольно ограниченный бот, давайте просто сыграем в игру?')


dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_help_command, commands='help')
dp.register_message_handler(process_stat_command, commands='stat')
dp.register_message_handler(process_cancel_command, commands='cancel')
dp.register_message_handler(process_positive_unswer, Text(equals=['Да', 'Давай', 'Сыграем', 'Игра', 'Играть', 'Хочу играть'], ignore_case=True))
dp.register_message_handler(process_negative_command, Text(equals=['Нет', 'Не', 'Не хочу'], ignore_case=True))
dp.register_message_handler(process_numbers_unswer, lambda x: x.text.isdigit() and 1 <= int(x.text) <= 100)
dp.register_message_handler(process_other_text_answers)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
