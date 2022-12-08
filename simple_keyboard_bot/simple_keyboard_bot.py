# A simple Telegram bot with keyboards
# https://stepik.org/lesson/759405/step/4?unit=761421

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType

from environs import Env


env = Env()
env.read_env()

BOT_TOKEN = env('BOT_TOKEN')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

keyboard.add(KeyboardButton(text='Отправить телефон', request_contact=True))
keyboard.add(KeyboardButton(text='Отправить геолокацию', request_location=True))
keyboard.add(KeyboardButton(text='Создать викторину', request_poll=KeyboardButtonPollType(type=types.PollType.QUIZ)))
keyboard.add(KeyboardButton(text='Создать опрос', request_poll=KeyboardButtonPollType(type=types.PollType.REGULAR)))


async def process_start_command(message: types.Message):
    await message.answer('Экспериментируем со специальными кнопками', reply_markup=keyboard)


dp.register_message_handler(process_start_command, commands='help')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
