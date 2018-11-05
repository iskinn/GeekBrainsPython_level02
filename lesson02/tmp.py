# 01

# import random

# SIZE = 10

# array = [random.randint(0, SIZE * SIZE)]

# array.sort()
# print(array)

# find = int(input('Введите число'))

# pos = len(array)
# left = 0
# right = len(array) - 1
# count = 0

# while array[pos] != find and lest <= right:
#     count += 1
#     if find > array[pos]

##############################
# 02

import random

SIZE = 10
array = [random.randint(0, SIZE * SIZE) for _ in range(SIZE)]
print(array)

num = int(input('Введите число: '))
pos = int(input('Введите позицию: '))

array.append(None)
i = len(array) - 1

while i > pos:
    array[i], array[i-1] = array[i-1], array[i]
    i -= 1
    print(array)

array[pos] = num
print(array)
