# Задача 2. поиск элемента по номеру по алгоритму Решето Эратосфена
# Закоментировал ввод номера числа и вывод самого числа, чтобы замерить производительность алгоритма

# timeit 01. n=10
# python3 -m timeit -n 100 -c "$(cat l_03.py)"
# 100 loops, best of 3: 35.9 usec per loop

# timeit 02. n=100
# python3 -m timeit -n 100 -c "$(cat l_03.py)"
# 100 loops, best of 3: 831 usec per loop

# timeit 03. n=1000
# python3 -m timeit -n 100 -c "$(cat l_03.py)"
# 100 loops, best of 3: 19.9 msec per loop

# cProfile 01. n=100
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#       542    0.000    0.000    0.000    0.000 l_03.py:28(IsPrime)
#         1    0.001    0.001    0.001    0.001 l_03.py:38(find_prime_number)
#         1    0.000    0.000    0.000    0.000 l_03.py:56(<listcomp>)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#      1638    0.000    0.000    0.000    0.000 {built-in method builtins.len}
#       542    0.000    0.000    0.000    0.000 {method 'append' of 'array.array' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile 01. n=1000
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.026    0.026 <string>:1(<module>)
#      7920    0.012    0.000    0.012    0.000 l_03.py:36(IsPrime)
#         1    0.010    0.010    0.026    0.026 l_03.py:46(find_prime_number)
#         1    0.000    0.000    0.000    0.000 l_03.py:64(<listcomp>)
#         1    0.000    0.000    0.026    0.026 {built-in method builtins.exec}
#     26949    0.002    0.000    0.002    0.000 {built-in method builtins.len}
#      7920    0.001    0.000    0.001    0.000 {method 'append' of 'array.array' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile 01. n=10000
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.597    0.597 <string>:1(<module>)
#    104730    0.405    0.000    0.405    0.000 l_03.py:45(IsPrime)
#         1    0.144    0.144    0.597    0.597 l_03.py:55(find_prime_number)
#         1    0.004    0.004    0.004    0.004 l_03.py:73(<listcomp>)
#         1    0.000    0.000    0.597    0.597 {built-in method builtins.exec}
#    384166    0.027    0.000    0.027    0.000 {built-in method builtins.len}
#    104730    0.018    0.000    0.018    0.000 {method 'append' of 'array.array' objects}
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
        numbers.append(i) # значениями от 0 до n-1
        if IsPrime(i):
            count_prime += 1
        i += 1

    numbers[1] = 0
    m = 2 # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < len(numbers): # перебор всех элементов до заданного числа
        if numbers[m] != 0: # если он не равен нулю, то
            j = m * 2 # увеличить в два раза (текущий элемент простое число)
            while j < len(numbers):
                numbers[j] = 0 # заменить на 0
                j = j + m # перейти в позицию на m больше
        m += 1
    primes = array('i', [i for i in numbers if i != 0])
    return primes[n-1]

#print('Это число: ', find_prime_number(100))
#find_prime_number(1000)

cProfile.run('find_prime_number(10000)')
