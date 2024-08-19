# Simple Telegram bot to demonstrate Telegram's messagy formatting options
# https://stepik.org/lesson/870035/step/1?unit=874213

from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message

from environs import Env


env = Env()
env.read_env('.env')

BOT_TOKEN = env('BOT_TOKEN')

# Можно один раз указать параметр pars_mode при инициализации:
# bot: Bot = Bot(BOT_TOKEN, parse_mode='HTML')
# или:
# bot: Bot = Bot(BOT_TOKEN, parse_mode='MarkdownV2')

bot: Bot = Bot(BOT_TOKEN)
dp: Dispatcher = Dispatcher(bot)

async def process_start_command(message: Message):
    await message.answer(
            text='Я бот, демонстрирующий '
                'как работает разметка. Отправь команду '
                'из списка ниже:\n\n'
                '/html - пример разметки с помощью HTML\n'
                '/markdownv2 - пример разметки с помощью MarkdownV2\n'
                '/noformat - пример с разметкой, но без указания '
                'параметра parse_mode'

    )


async def process_help_command(message: Message):
    await message.answer(
            text='Я бот, демонстрирующий '
                'как работает разметка. Отправь команду '
                'из списка ниже:\n\n'
                '/html - пример разметки с помощью HTML\n'
                '/markdownv2 - пример разметки с помощью MarkdownV2\n'
                '/noformat - пример с разметкой, но без указания '
                'параметра parse_mode'
    )


async def process_html_command(message: Message):
    await message.answer(
            text='Это текст, демонстрирующий '
                'как работает HTML-разметка:\n\n'
                '<b>Это жирный текст</b>\n'
                '<i>Это наклонный текст</i>\n'
                '<u>Это подчеркнутый текст</u>\n'
                '<span class="tg-spoiler">А это спойлер</span>\n\n'
                'Чтобы еще раз посмотреть список доступных команд - '
                'отправь команду /help',
            parse_mode='HTML'
    )


async def process_markdownv2_command(message: Message):
    await message.answer(
            text='Это текст, демонстрирующий '
                'как работает MarkdownV2\-разметка:\n\n'
                '*Это жирный текст*\n'
                '_Это наклонный текст_\n'
                '__Это подчеркнутый текст__\n'
                '||А это спойлер||\n\n'
                'Чтобы еще раз посмотреть список доступных команд \- '
                'отправь команду /help',
            parse_mode='MarkdownV2'
    )


async def process_noformat_command(message: Message):
    await message.answer(
            text='Это текст, демонстрирующий '
                'как отображается текст, если не указать '
                'параметр parse_mode:\n\n'
                '<b>Это мог бы быть жирный текст</b>\n'
                '_Это мог бы быть наклонный текст_\n'
                '<u>Это мог бы быть подчеркнутый текст</u>\n'
                '||А это мог бы быть спойлер||\n\n'
                'Чтобы еще раз посмотреть список доступных команд - '
                'отправь команду /help'
    )


async def send_echo(message: Message):
    await message.answer(
            text='Я даже представить себе не могу, '
                'что ты имеешь в виду\n\n'
                'Чтобы посмотреть список доступных команд - '
                'отправь команду /help'
    )


dp.register_message_handler(process_start_command,
                            commands='start')
dp.register_message_handler(process_help_command,
                            commands='help')
dp.register_message_handler(process_html_command,
                            commands='html')
dp.register_message_handler(process_markdownv2_command,
                            commands='markdownv2')
dp.register_message_handler(process_noformat_command,
                            commands='noformat')
dp.register_message_handler(send_echo,
                            content_types='any')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
