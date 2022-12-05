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
