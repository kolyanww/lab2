import math

def calculate_e(a, m, b):
    """Обчислює очікуване значення для завдання."""
    return (a + 4 * m + b) / 6

def calculate_sd(a, b):
    """Обчислює стандартне відхилення для завдання."""
    return (b - a) / 6

def calculate_ci(tasks):
    """Обчислює довірчий інтервал для проекту."""
    # Обчислення очікуваного значення та стандартного відхилення для кожного завдання
    e_values = []
    sd_values = []
    for task in tasks:
        e_values.append(calculate_e(*task))
        sd_values.append(calculate_sd(task[0], task[2]))

    # Обчислення очікуваного значення та стандартного відхилення для проекту
    e_project = sum(e_values)
    sd_project = math.sqrt(sum([sd ** 2 for sd in sd_values]))

    # Обчислення довірчого інтервалу для проекту
    ci_min = e_project - 2 * sd_project
    ci_max = e_project + 2 * sd_project

    return ci_min, ci_max

# Запит користувача на введення оцінок завдань
tasks = []
while True:
    a = float(input("Введіть оцінку 'a' для завдання: "))
    m = float(input("Введіть оцінку 'm' для завдання: "))
    b = float(input("Введіть оцінку 'b' для завдання: "))
    tasks.append((a, m, b))

    # Запит користувача на введення наступного завдання
    another_task = input("Бажаєте ввести ще одне завдання? (так/ні) ")
    if another_task.lower() != "так":
        break

# Обчислення довірчого інтервалу для проекту
ci_min, ci_max = calculate_ci(tasks)

# Виведення результату
print(f"Довірчий інтервал проекту (95%): {ci_min:.2f} ... {ci_max:.2f} балів")
