Создайте структуру проекта пакетом 
src/, виртуальное окружение, файл 
.gitignore, разместите TXT-файл в папке 
data/, сделайте первый коммит.

Напишите функцию, которая принимает имя файла
и возвращает список имен, содержащихся 
в файле. Файл содержит имена на разных 
языках и может содержать знаки препинания 
вокруг имен, пустые строки и цифры. 
Функция должна удалить знаки препинания 
и цифры и возвращать только строки, 
содержащие имя. Сделайте новый коммит. 
В отдельном коммите измените TXT-файл, 
сделав его меньше для простоты тестирования.

Напишите другие функции, позволяющие из списка 
имен получать только русские и английские и 
записывать эти имена в файл в отсортированном 
виде. В итоге программа должна считывать данные 
из исходного файла и формировать два файла с 
русскими и английскими именами, отсортированными 
по алфавиту. Новые файлы должны создаваться в 
папке data/. Всегда делайте точечные коммиты. 
После завершения разработки сделайте отмену 
коммита, в котором был урезан исходный файл, 
т. е. верните полный TXT-файл.
Установите Flake8 и mypy. Проверьте ими ваш код. 
Если Flake8 выдает ошибки, устраните их с 
помощью инструмента black. Через git diff 
посмотрите, как black отформатировал ваш код. 
Добавьте аннотации типов. mypy не должен 
выдавать ошибки.