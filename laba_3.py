import sys


def find_pairs(numbers):
    pairs = []
    numbers_set = set(numbers)  # перетворюємо список чисел в множину для швидшого доступу до елементів

    for num in numbers_set:
        complement = 10 - num  # шукаємо доповнення до поточного числа, щоб отримати суму 10

        if complement in numbers_set:  # перевіряємо, чи є доповнення в множині чисел
            pair = (num, complement)
            pairs.append(pair)

    return pairs


if __name__ == '__main__':
    numbers = list(map(int, sys.argv[1:]))  # отримуємо числа з аргументів командного рядка

    pairs = find_pairs(numbers)

    for pair in pairs:
        print(f"{pair[0]} + {pair[1]}")
