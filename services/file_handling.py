import os

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    marks = '...,;:?!'
    if text[:size][-1] in marks and text[:size+1][-1] not in marks:
        answer = ''.join(text[start:start+size+1])
        count = len(answer.strip())
        return (answer,count)
    else:
        while text[:start + size][-1] not in marks or text[:size+1][-1] in marks:
            size -= 1
        answer = ''.join(text[start:start + size])
        count = len(answer.strip())
        return (answer,count)


with open("test.txt", encoding="utf8") as r:
    text = r.read()
    print(*_get_part_text(text, 5, 9), sep='\n')
# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    pass


# Вызов функции prepare_book для подготовки книги из текстового файла
# prepare_book(os.path.join(os.getcwd(), BOOK_PATH))