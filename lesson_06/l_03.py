# Посчитать, сколько раз встречается определенная цифра в 
# введенной последовательности чисел. 
# Количество вводимых чисел и цифра, 
# которую необходимо посчитать, задаются вводом с клавиатуры. 

import sys

def show_size(x, level=0):
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}, ref_count = {sys.getrefcount(x)}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x,str):
            for item in x:
                show_size(item, level + 1)

n = input('Введите число: ')
x = input('Какое число посчитать: ')
count = 0

for i in n:
    if i == x:
        count += 1

print (f'Количество: {count}')

show_size(n)
show_size(x)
show_size(i)
show_size(count)


# Введите число: 234325454656
# Какое число посчитать: 2
# Количество: 2
#  type = <class 'str'>, size = 61, object = 234325454656, ref_count = 5
#  type = <class 'str'>, size = 50, object = 2, ref_count = 6
#  type = <class 'str'>, size = 50, object = 6, ref_count = 6
#  type = <class 'int'>, size = 28, object = 2, ref_count = 115

# Вывод: в этой задаче используются только переменные. 
# Из расхода памяти видно, что гипотетически использовав переменные числового типа int, 
# расход памяти можно снизить. Но в данной задаче я не вижу как это сделать.