from aiogram import Router, Bot
from aiogram.filters import Command, Text, CommandStart
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, InputMediaAudio,
                           InputMediaDocument, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.exceptions import TelegramBadRequest

router: Router = Router()

LEXICON: dict[str, str] = {
    'audio': '🎶 Аудио',
    'text': '📃 Текст',
    'photo': '🖼 Фото',
    'video': '🎬 Видео',
    'document': '📑 Документ',
    'voice': '📢 Голосовое сообщение',
    'text_1': 'Это обыкновенное текстовое сообщение, его можно легко отредактировать другим текстовым сообщением, но нельзя отредактировать сообщением с медиа.',
    'text_2': 'Это тоже обыкновенное текстовое сообщение, которое можно заменить на другое текстовое сообщение через редактирование.',
    'photo_id1': 'AgACAgIAAxkBAAIDQmSQIqbYeszx-mW7-QnDWpBhhRaBAAJZyjEblNmASGjMtZPMm4tOAQADAgADeQADLwQ ',
    'photo_id2': 'AgACAgIAAxkBAAIDRGSQIq4n2yzb3VBNyCZI3puL1GE7AAJbyjEblNmASMpE8z3-CvegAQADAgADeQADLwQ',
    'document_id1': 'BQACAgIAAxkBAAIDSGSQItNEBvwqPD8VGs9TsRQGkFkxAAKgMQAClNmASBsR0DiIi5GzLwQ ',
    'document_id2': 'BQACAgIAAxkBAAIDSmSQIuAMJf3SEUboQBRWGnm9BRaSAAKhMQAClNmASMVIVzN2x502LwQ',
    }

info: dict[str, list] = {
    'document': [],
    'photo': []
}

# Функция для генерации клавиатур с инлайн-кнопками
def get_markup(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []
    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))
    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Этот хэндлер будет срабатывать на команду "/start"
@router.message(CommandStart())
async def process_start_command(message: Message):
    markup = get_markup(2, 'photo')
    await message.answer_photo(
                        photo=LEXICON['photo_id1'],
                        caption='Это фото 1',
                        reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@router.callback_query(Text(text=['text',
                              'audio',
                              'video',
                              'document',
                              'photo',
                              'voice']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = get_markup(2, 'photo')
    try:
        await bot.edit_message_media(
                            chat_id=callback.message.chat.id,
                            message_id=callback.message.message_id,
                            media=InputMediaPhoto(
                                    media=LEXICON['photo_id2'],
                                    caption='Это фото 2'),
                            reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
                            chat_id=callback.message.chat.id,
                            message_id=callback.message.message_id,
                            media=InputMediaPhoto(
                                    media=LEXICON['photo_id1'],
                                    caption='Это фото 1'),
                            reply_markup=markup)