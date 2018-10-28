import random

x = int(input ("Введите начало диапазона для целого числа: "))
y = int(input ("Введите конец диапазона для целого числа: "))
n = random.randint(x, y)
print("Случайное целое число из диапазона = ", n)

x = int(input ("Введите начало диапазона для вещественного числа: "))
y = int(input ("Введите конец диапазона для вещественного числа: "))
m = random.uniform(x, y)
print("Случайное вещественное число из диапазона = ", m)

x = input ("Введите симвод начало диапазона: ")
y = input ("Введите символ конец диапазона: ")
simbol_start = ord(x)
simbol_end = ord(y)
n = random.randint(simbol_start, simbol_end)
simbol = chr(n)
print("Случайный символ = ", simbol)
