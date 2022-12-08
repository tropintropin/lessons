# A simple Telegram bot with keyboards
# https://stepik.org/lesson/759405/step/2?unit=761421

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton, KeyboardButtonPollType

from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True)

button1 = KeyboardButton('Собак 🦮')
button2 = KeyboardButton('Огурцов 🥒')


keyboard.add(button1, button2)

async def process_start_command(message: types.Message):
    await message.answer('Чего кошки боятся больше?', reply_markup=keyboard)


async def process_dog_answer(message: types.Message):
    await message.answer(
        'Да, несомненно, кошки боятся собак. Но вы видели как они боятся огурцов?',
        reply_markup=ReplyKeyboardRemove()
        )


async def process_cucumber_answer(message: types.Message):
    await message.answer(
        'Да, иногда кажется, что огурцов кошки боятся больше',
        reply_markup=ReplyKeyboardRemove()
        )


dp.register_message_handler(process_start_command, commands='start')
dp.register_message_handler(process_dog_answer, text='Собак 🦮')
dp.register_message_handler(process_cucumber_answer, text='Огурцов 🥒')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
