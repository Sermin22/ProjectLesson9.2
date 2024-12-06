import os
import re


def clear_names(file_names: str) -> list:
    """Функция для очистки имен от лишних символов"""
    PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "Data", file_names)
    with open(PATH_TO_FILE, "r", encoding="utf-8") as file:
        list_file_names = file.read().split()
        new_file_names = []
        for names in list_file_names:
            new_names = ""
            for name in names:
                if name.isalpha():
                    new_names += name
            if new_names.isalpha():
                new_file_names.append(new_names)
    return new_file_names


def is_cyrillic(name: str) -> bool:
    """Проверка на вхождение кирилицы в строку"""
    return bool(re.search("[а-яА-Я]", name))


def filter_russian_names(file_clear_names: list) -> list:
    """Формирования списка с русскими именами"""
    new_file_names = []
    for name in file_clear_names:
        if is_cyrillic(name):
            new_file_names.append(name)
    return new_file_names


def filter_english_names(file_clear_names: list) -> list:
    """Формирования текста с английскими именами"""
    new_file_names = []
    for name in file_clear_names:
        if not is_cyrillic(name):
            new_file_names.append(name)
    return new_file_names


def save_to_file(file_names: str, names: str) -> None:
    """Запись файла txt с именами"""
    PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "Data", file_names)
    with open(PATH_TO_FILE, "w", encoding="utf-8") as file:
        file.write(names)


if __name__ == "__main__":
    list_clear_names = clear_names("names.txt")

    russian_names = filter_russian_names(list_clear_names)
    save_to_file("russian_names.txt", "\n".join(russian_names))

    english_names = filter_english_names(list_clear_names)
    save_to_file("english_names.txt", "\n".join(english_names))
