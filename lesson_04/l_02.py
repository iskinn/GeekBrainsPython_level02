# ДЗ 03. Задача 1.
# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны любому из чисел в диапазоне от 2 до 9.

# Вариант 1. С использованием словаря и диапазона range(2,n)
# Замеры cprofile

# Замер 1. n = 100
# cProfile.run('find_multiple(100)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     1    0.000    0.000    0.000    0.000 l_02.py:39(find_multiple)
#     1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#   187    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Замер 2. n = 1000
# cProfile.run('find_multiple(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     1    0.001    0.001    0.001    0.001 l_02.py:39(find_multiple)
#     1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#  1922    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Замер 3. n = 10000
# cProfile.run('find_multiple(10000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#     1    0.000    0.000    0.011    0.011 <string>:1(<module>)
#     1    0.010    0.010    0.011    0.011 l_02.py:39(find_multiple)
#     1    0.000    0.000    0.011    0.011 {built-in method builtins.exec}
# 19283    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

import cProfile

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

cProfile.run('find_multiple(10000)')


#  Вариант 2. С использованием словаря и списка (2,n)

# 1. n = 100
# cProfile.run('find_multiple(100)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 l_02.py:60(find_multiple)
#         1    0.000    0.000    0.000    0.000 l_02.py:61(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#       187    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 2. n = 1000
# cProfile.run('find_multiple(1000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 l_02.py:69(find_multiple)
#         1    0.000    0.000    0.000    0.000 l_02.py:70(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1922    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 3. n = 10000
# cProfile.run('find_multiple(10000)')
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#         1    0.007    0.007    0.009    0.009 l_02.py:76(find_multiple)
#         1    0.001    0.001    0.001    0.001 l_02.py:77(<listcomp>)
#         1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#     19283    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

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

# cProfile.run('find_multiple(10000)')


# Вывод:
# В испытании видно что время первого варианта выше на 18%.
# Конечно этому есть объяснение: цикл for 
# или использование range вместо заранее сгенеренного списка.
# Сложность O (x)