def analyze_file(file_path):: Цей рядок визначає функцію analyze_file, яка приймає шлях до файлу file_path як аргумент.

try:: Цей рядок починає блок try-except, який використовується для обробки виключень.

with open(file_path, 'r') as file:: Цей рядок відкриває файл за заданим шляхом file_path в режимі читання і призначає йому ім'я file. Відкритий файл автоматично закриється після виконання блоку with.

lines = file.readlines(): Цей рядок зчитує усі рядки файлу із змінної file і зберігає їх у список lines.

total_lines = len(lines): Цей рядок обчислює загальну кількість рядків у файлі, використовуючи функцію len().

empty_lines = lines.count('\n'): Цей рядок обчислює кількість порожніх рядків у файлі, використовуючи метод count() для підрахунку символу нового рядка '\n'.

lines_with_z = sum('z' in line for line in lines): Цей рядок обчислює кількість рядків, що містять літеру 'z', використовуючи генератор списку та функцію sum().

total_z_count = sum(line.count('z') for line in lines): Цей рядок обчислює загальну кількість входжень літери 'z' у всіх рядках файлу, використовуючи генератор списку та функцію sum().

lines_with_and = sum('and' in line for line in lines): Цей рядок обчислює кількість рядків, що містять групу символів 'and', використовуючи генератор списку та функцію sum().

print(f"File: {file_path}"): Цей рядок виводить назву файлу, що аналізується.

print(f"Total lines: {total_lines}"): Цей рядок виводить загальну кількість рядків у файлі.

print(f"Empty lines: {empty_lines}"): Цей рядок виводить кількість порожніх рядків у файлі.

print(f"Lines with 'z': {lines_with_z}"): Цей рядок виводить кількість рядків, що містять літеру 'z'.

print(f"'z' count: {total_z_count}"): Цей рядок виводить загальну кількість входжень літери 'z' у файлі.

print(f"Lines with 'and': {lines_with_and}"): Цей рядок виводить кількість рядків, що містять групу символів 'and'.

except FileNotFoundError:: Цей рядок вказує, що обробляти виключення, якщо файл не знайдено.

print(f"File '{file_path}' not found."): Цей рядок виводить повідомлення про те, що файл не знайдено.

while True:: Цей рядок починає цикл, який триває безкінечно.

file_path = input("Enter the file path: "): Цей рядок запитує в користувача шлях до файлу для аналізу.

analyze_file(file_path): Цей рядок викликає функцію analyze_file для аналізу вказаного файлу.

choice = input("Do you want to analyze another file? (Yes/No): "): Цей рядок запитує користувача, чи потрібно аналізувати інший файл.

if choice.lower() != 'yes':: Цей рядок перевіряє, чи відповідь користувача не є 'yes'.

break: Цей рядок завершує цикл.


Якщо виконати цей код і ввести шлях до файлу "./storage/run2019.txt", а потім відповісти "No" на запит про аналіз іншого файлу, отримаємо такий результат:

Enter the file path: ./storage/run2019.txt
File: ./storage/run2019.txt
Total lines: 10
Empty lines: 4
Lines with 'z': 4
'z' count: 34
Lines with 'and': 3

Do you want to analyze another file? (Yes/No): No
