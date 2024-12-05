# тест для проверки как работает импорт одной функции из модуля main
from main import clear_names

list_clear_names = clear_names("names2.txt")
for names in list_clear_names:
    print(names)