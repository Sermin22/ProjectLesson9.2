# код для очистки имен от лишних символов
import os

PATH_TO_FILE = os.path.join(os.path.dirname(__file__), "Data", "names.txt")
with open(PATH_TO_FILE, "r", encoding="utf-8") as file:

# file_txt = "names.txt"
# with open("data/" + file_txt, "r", encoding="utf-8") as file:
    list_file_names = file.read().split()
    new_file_names = []
    for names in list_file_names:
        new_names = ""
        for name in names:
            if name.isalpha():
                new_names += name
        if new_names.isalpha():
            new_file_names.append(new_names)

print(new_file_names)
