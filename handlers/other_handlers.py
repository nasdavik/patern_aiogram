from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

router: Router = Router()


# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    await message.answer(text=f"Я все о тебе знаю \n"
                              f"Твой user_id = {message.from_user.id}")