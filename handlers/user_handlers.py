from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from create_disp import dp
from lexicon.lexicon import LEXICON_RU


# Этот хэндлер срабатывает на команду /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


# Этот хэндлер срабатывает на команду /help
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])