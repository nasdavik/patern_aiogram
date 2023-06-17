from aiogram import Router
from aiogram.filters import Command, CommandStart, Text
from aiogram.types import Message
from aiogram import F

router: Router = Router()

info: dict[str, list] = {
    'audio': [],
    'video': [],
    'voice': [],
    'document': []
}

@router.message()
async def hunting_type(message: Message):
    await message.answer(text=message.content_type)

