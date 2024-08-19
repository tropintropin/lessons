from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import CallbackQuery, Message, PollAnswer

from lexicon import LEXICON, LEXICON_POLL
from keyboards import create_passwords_keyboard
from services import create_password


router: Router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON[message.text],
        reply_markup=create_passwords_keyboard()
    )


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(
        text=LEXICON[message.text],
        reply_markup=create_passwords_keyboard()
    )


@router.callback_query(Text(text='create_password'))
async def process_create_password_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=f'Ваш пароль:\n<code>{create_password()}</code>',
        reply_markup=create_passwords_keyboard(),
        parse_mode='HTML'
    )


@router.callback_query(Text(text='create_castom'))
async def process_create_castom_press(callback: CallbackQuery):
    await callback.message.answer_poll(
        question=LEXICON['user_settings'],
        options=list(LEXICON_POLL.values()),
        allows_multiple_answers=True,
        is_anonymous=False
    )


# TODO: Доделать получение результатов квиза и передачу их
# в create_password()
# @router.callback_query(PollAnswer())
# async def process_get_poll(callback: CallbackQuery):
#     await callback.message.answer(text=PollAnswer())


@router.callback_query(Text(text='cancel'))
async def process_cancel_press(callback: CallbackQuery):
    pass
