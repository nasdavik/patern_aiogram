from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from lexicon.lexicon import LEXICON_RU

# Клавиатура для ответов
answer_btns = [KeyboardButton(text=f"{LEXICON_RU['yes_button']}")]
answer_kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
answer_kb.row(*answer_btns, width=1)
answer_keyboard: ReplyKeyboardMarkup = answer_kb.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)


# Клавиатура для игры
game_btns = [KeyboardButton(text=f"{x}") for x in (LEXICON_RU['rock'], LEXICON_RU['paper'],
                                                   LEXICON_RU['scissors'])]
game_kb: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
game_kb.row(*game_btns, width=1)
game_keyboard: ReplyKeyboardMarkup = game_kb.as_markup(
    resize_keyboard=True)

