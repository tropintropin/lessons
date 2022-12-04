# Эхо-бот [aiogram]
# https://stepik.org/lesson/759399/step/1?unit=761415
# https://stepik.org/lesson/759399/step/3?unit=761415
# My Solution

from aiogram import Bot, Dispatcher, executor, types
import re


def get_token(url: str) -> str:
    with open(url) as bt:
        return re.search(r'(?<=BOT_TOKEN=)\w+:\w+$', [line for line in bt][0])[0]


API_TOKEN = get_token('.env')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])  # /start command
async def process_start_command(message: types.Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


@dp.message_handler(commands=['help'])  # /help command
async def process_help_command(message: types.Message):
    await message.answer('Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')


@dp.message_handler()  # any commands exept /start & /help
async def send_eho(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
