"""A simple Telegram bot for guessing numbers from 1 to 100
https://stepik.org/lesson/759400/step/1?unit=761416
https://stepik.org/lesson/759400/step/2?unit=761416
https://stepik.org/lesson/759400/step/3?unit=761416
https://stepik.org/lesson/759400/step/5?unit=761416
"""

import random
import re

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.dispatcher.filters import Text


def get_token(url: str) -> str:
    with open(url) as bt:
        return re.search(
            r'(?<=BOT_TOKEN=)\w+:\w+$', [line for line in bt][0]
            )[0]


API_TOKEN = get_token('.env')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)