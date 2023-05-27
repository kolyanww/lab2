def analyze_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()  # Зчитування усіх рядків файлу в список

            total_lines = len(lines)  # Обчислення загальної кількості рядків
            empty_lines = lines.count('\n')  # Обчислення кількості порожніх рядків
            lines_with_z = sum('z' in line for line in lines)  # Обчислення кількості рядків з літерою 'z'
            total_z_count = sum(line.count('z') for line in lines)  # Обчислення загальної кількості літер 'z' у файлі
            lines_with_and = sum('and' in line for line in lines)  # Обчислення кількості рядків з групою символів 'and'

            # Виведення статистики
            print(f"File: {file_path}")
            print(f"Total lines: {total_lines}")
            print(f"Empty lines: {empty_lines}")
            print(f"Lines with 'z': {lines_with_z}")
            print(f"'z' count: {total_z_count}")
            print(f"Lines with 'and': {lines_with_and}")
            print()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

while True:
    file_path = input("Enter the file path: ")
    analyze_file(file_path)  # Виклик функції analyze_file для аналізу вказаного файлу

    choice = input("Do you want to analyze another file? (Yes/No): ")
    if choice.lower() != 'yes':
        break
