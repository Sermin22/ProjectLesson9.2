# код дублирующий функции из main.py, но путь открытыя файла txt выполнен иначе
import re


def clear_names(file_names: str) -> list:
    """Функция для очистки имен от лишних символов"""
    with open("data/" + file_names, "r", encoding="utf-8") as file:
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
    """ Проверка на вхождение кирилицы в строку """
    return bool(re.search("[а-яА-Я]", name))


def filter_russian_names(file_clear_names: list) -> list:
    new_file_names = []
    for name in file_clear_names:
        if is_cyrillic(name):
            new_file_names.append(name)
    return new_file_names


def filter_english_names(file_clear_names: list) -> list:
    new_file_names = []
    for name in file_clear_names:
        if not is_cyrillic(name):
            new_file_names.append(name)
    return new_file_names


def save_to_file(file_names: str, names: str) -> None:
    with open("data/" + file_names, "w", encoding="utf-8") as file:
        file.write(names)


# if __name__ == "__main__":
#     list_clear_names = clear_names("names.txt")
#
#     russian_names = filter_russian_names(list_clear_names)
#     save_to_file("russian_names.txt", "\n".join(russian_names))
#
#     english_names = filter_english_names(list_clear_names)
#     save_to_file("english_names.txt", "\n".join(english_names))
