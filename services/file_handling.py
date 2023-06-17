import os
import math
import pprint

BOOK_PATH = 'C:\\Users\\1\\PycharmProjects\\patern_aiogram\\book\\book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    marks = '...,;:?!'
    while text[:start + size][-1] not in marks or text[:size+1][-1] in marks:
        size -= 1
    answer = ''.join(text[start:start + size])
    count = len(answer.strip())
    return (answer.strip(), count)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, encoding="utf8") as r:
        r = r.read()
        start = 0
        for page in range(math.ceil(len(r.strip()) / PAGE_SIZE)):
            answer = _get_part_text(r, start, PAGE_SIZE)
            book[page+1] = answer[0].strip()
            start += answer[1]

# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))
