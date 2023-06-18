from aiogram import Router
from aiogram.filters import Command, Text
from aiogram.types import Message
from aiogram import F

router: Router = Router()

point = 0

info: dict[str, list] = {
    'audio': [],
    'voice': [],
    'document': [],
    'photo': []
}


@router.message(Command(commands="info"))
async def take_info(message: Message):
    await message.answer(text="\n".join([" ".join(x) for x in info.values()]))


@router.message(F.content_type == 'voice')
async def hunting_type(message: Message):
    info['voice'].append(message.voice.file_id)
    await message.answer(text=message.content_type)


@router.message(F.content_type == 'photo')
async def hunting_type(message: Message):
    answer = [x for x in list(message.photo[-1])]
    info['photo'].append(answer[0][1])
    await message.answer(text=message.content_type)


@router.message(F.content_type == 'document')
async def hunting_type(message: Message):
    info['document'].append(message.document.file_id)
    await message.answer(text=message.content_type)

@router.message(Text(text='photo'))
async def send_photo(message: Message):
    await message.answer_photo(info['photo'][-1])