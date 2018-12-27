# ДЗ 03. Задача 1.
# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

# Вариант 1. С использованием словаря и диапазона range(2,n)
# Замеры timeit

# Замер 1. n = 100
#  python3 -m timeit -n 100 -c "$(cat l_01.py)"
# 100 loops, best of 3: 71.1 usec per loop

# Замер 2. n = 1000
#  python3 -m timeit -n 100 -c "$(cat l_01.py)"
# 100 loops, best of 3: 846 usec per loop

# Замер 3. n = 10000
#  python3 -m timeit -n 100 -c "$(cat l_01.py)"
# 100 loops, best of 3: 8.59 msec per loop


multiple = {}

def find_multiple(n):
    spam = []
    for x in range(2,11):
        for y in range(2,n):
            if y % x == 0:
                spam.append(y)
        multiple[x] = spam
        spam = []
    return multiple

find_multiple(10000)


#  Вариант 2. С использованием словаря и списка (2,n)

# 1. n = 100
#  python3 -m timeit -n 100 -c "$(cat l_01.py)"
# 100 loops, best of 3: 70.9 usec per loop

# 2. n = 1000
# python3 -m timeit -n 100 -c "$(cat l_01.py)"
# 100 loops, best of 3: 690 usec per loop

# 3. n = 10000
#  python3 -m timeit -n 100 -c "$(cat l_01.py)"
# 100 loops, best of 3: 6.95 msec per loop

# def find_multiple(n):
#     natural_numbers = [i for i in range(2,n)]
#     multiple = {}
#     spam = []
#     x = 2
#     while x <= 10:
#         for y in natural_numbers:
#             if y % x == 0:
#                 spam.append(y)
#         multiple[x] = spam
#         spam = []
#         x += 1
#     return multiple

# find_multiple(100)