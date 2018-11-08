# Задача 2. поиск элемента по номеру по алгоритму без Решета Эратосфена
# Закоментировал ввод номера числа и вывод самого числа, чтобы замерить производительность алгоритма

# timeit 01. n=10
# python3 -m timeit -n 100 -c "$(cat l_04.py)"
# 100 loops, best of 3: 16.9 usec per loop

# timeit 02. n=100
# python3 -m timeit -n 100 -c "$(cat l_04.py)"
# 100 loops, best of 3: 445 usec per loop

# timeit 03. n=1000
# python3 -m timeit -n 100 -c "$(cat l_04.py)"
# 100 loops, best of 3: 13.3 msec per loop

# cProfile 01. n=100
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       542    0.000    0.000    0.000    0.000 l_04.py:26(IsPrime)
#         1    0.000    0.000    0.001    0.001 l_04.py:36(find_prime_number)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile 01. n=1000
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.015    0.015 <string>:1(<module>)
#      7920    0.013    0.000    0.013    0.000 l_04.py:32(IsPrime)
#         1    0.002    0.002    0.015    0.015 l_04.py:42(find_prime_number)
#         1    0.000    0.000    0.015    0.015 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile 01. n=10000
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.457    0.457 <string>:1(<module>)
#    104730    0.427    0.000    0.427    0.000 l_04.py:38(IsPrime)
#         1    0.029    0.029    0.457    0.457 l_04.py:48(find_prime_number)
#         1    0.000    0.000    0.457    0.457 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

import cProfile
from array import array

# Функция для определения является ли число простым. Возвращает True или False
def IsPrime(n):
   d = 2
   while d * d <= n and n % d != 0:
       d += 1
   return d * d > n

#n = int(input("Введите номер простого числа для его вывода: "))

numbers = array('i')

def find_prime_number(n):
    count_prime = 0
    i = 0
    while count_prime <= n+1:
        if IsPrime(i):
            count_prime += 1
        i += 1
    return i-1

#print('Это число: ', find_prime_number(100))
#find_prime_number(100)

cProfile.run('find_prime_number(1000)')

# Вывод:
# В испытании видно что время первого варианта выше на 23%.
# Сложность O(x)