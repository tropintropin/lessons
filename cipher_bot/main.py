'''A primitive password generator Telegram bot
for SkillFactory webinars 2023.03.01—03
Features:
choice of password length (with type checking),
the ability for the user to exclude unwanted characters,
the ability to create multiple passwords.
Author: Valery Tropin, tropin.tropin@gmail.com
'''

import asyncio

import handlers

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from keyboards import set_main_menu


async def main():
    bot: Bot = Bot(token=BOT_TOKEN)
    dp: Dispatcher = Dispatcher()

    await set_main_menu(bot)

    dp.include_router(handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
