from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from lexicon.lexicon import LEXICON_RU
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Инициализируем роутер уровня модуля
router: Router = Router()

# Добавим кнопки
btns = [KeyboardButton(text=f"{x}") for x in ("Камень", "Ножницы", "Бумага")]

# Создаем билдер с кнопками
keyboard: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

keyboard.row(*btns, width=3)

# Создаем объект клавиатуры, добавляя в него кнопки
my_keyboard: ReplyKeyboardMarkup = keyboard.as_markup(
    resize_keyboard=True)


# Этот хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=my_keyboard)


# Этот хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


