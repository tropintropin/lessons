# https://stepik.org/lesson/759408/step/14?unit=761424

from aiogram import Dispatcher
from aiogram.types import Message


async def send_echo(message: Message):
    await message.answer(f'''Это эхо! {message.text}
    Используйте команду /help, чтобы увидеть справку.''')


def register_echo_handler(dp: Dispatcher):
    dp.register_message_handler(send_echo)
