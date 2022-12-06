"""Эхо-бот [aiogram]
https://stepik.org/lesson/759399/step/1?unit=761415 — create bot
https://stepik.org/lesson/759399/step/3?unit=761415 — handlers register
https://stepik.org/lesson/759399/step/4?unit=761415 — add photos handler
"""

import re

from aiogram import Bot, Dispatcher, executor, types


def get_token(url: str) -> str:
    with open(url) as bt:
        return re.search(
            r'(?<=BOT_TOKEN=)\w+:\w+$', [line for line in bt][0]  # pyright: ignore
            )[0]


API_TOKEN = get_token('.env')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])  # /start command
async def process_start_command(message: types.Message):
    await message.answer(
        'Привет! Я Эхо-бот.\nНапиши мне что-нибудь, пришли картинку, фото, mp3, либо запиши войс, и я отправлю их тебе в ответ :-)')


@dp.message_handler(commands=['help'])  # /help command
async def process_help_command(message: types.Message):
    await message.answer(
        'Напиши мне что-нибудь и в ответ я пришлю тебе твое сообщение')


@dp.message_handler(content_types=['photo'])  # eho photo
async def send_photo_eho(message: types.Message):
    await message.reply_photo(message.photo[0].file_id)


@dp.message_handler(content_types=['audio'])  # eho .mp3
async def send_audio_eho(message: types.Message):
    await message.reply_audio(message.audio.file_id)


@dp.message_handler(content_types=['voice'])
async def send_voice_eho(message: types.Message):
    await message.reply_voice(message.voice.file_id)


@dp.message_handler()  # eho text
async def send_eho(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
