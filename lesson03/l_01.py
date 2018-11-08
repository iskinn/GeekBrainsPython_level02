import random

a = []

for x in range(2,10):
    for y in range(2,100):
        if y % x == 0:
                a.append(y)
    print(f'Кратные числа числу x = {x}: ',' '.join(map(str, a)))
    a = []
