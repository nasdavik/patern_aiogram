import os

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    marks = '...,;:?!'
    if text[:start + size][-1] in marks and text[:start + size+1][-1] not in marks:
        answer = ''.join(text[start:start+size+1])
        count = len(answer.strip())
        return (answer.strip(), count)
    else:
        while text[:start + size][-1] not in marks or text[:size+1][-1] in marks:
            size -= 1
        answer = ''.join(text[start:start + size])
        count = len(answer.strip())
        return (answer.strip(), count)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    pass


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(os.getcwd(), BOOK_PATH))