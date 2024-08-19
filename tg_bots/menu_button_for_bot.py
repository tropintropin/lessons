# Add menu button to your Telegram bot
# https://stepik.org/lesson/792844/step/1?unit=795518

from aiogram import Bot, Dispatcher, executor, types
from environs import Env


env = Env()
env.read_env()

BOT_TOKEN: str = env('BOT_TOKEN')

bot: Bot = Bot(token=BOT_TOKEN)
dp: Dispatcher = Dispatcher(bot)

async def set_main_menu(dp: Dispatcher):
    main_menu_commands = [
        types.BotCommand(command='/start', description='Запустить бота'),
        types.BotCommand(command='/help', description='Справка по работе бота')
    ]
    await dp.bot.set_my_commands(main_menu_commands)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=set_main_menu)
