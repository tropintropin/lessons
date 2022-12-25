# https://stepik.org/lesson/759408/step/7?unit=761424
# https://stepik.org/lesson/759408/step/8?discussion=6823054&thread=solutions&unit=761424
# https://stepik.org/lesson/759408/step/9?discussion=6827447&thread=solutions&unit=761424

import re


BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, size: int) -> tuple[str, int]:
    while True:
        page = text[start:start+size]
        page_esq = re.escape(page)
        if re.search(rf'{page_esq}(?=[.,!?:;])', text[start:]):
            size -= 1
            continue
        break

    while page:
        if re.search(r'(?<=\w)[.!?][.]{2}\Z', page):
            break
        elif re.search(r'[.,!?:;]{2}\Z', page):
            page = page[:-2]
        elif re.search(r'(?<=\w)[.,!?:;]\Z', page):
            break
        else:
            page = page[:-1]
    return page, len(page)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(path, mode='r', encoding='utf-8') as f:
        text: str = f.read()

    page_counter: int = 1
    start: int = 0
    while True:
        page, size = _get_part_text(text, start, PAGE_SIZE)
        if page:
            book.update({page_counter: page.lstrip()})
            page_counter += 1
            start += size
        else:
            break


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(BOOK_PATH)
