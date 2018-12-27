import sys
from array import array

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

numbers = array('i',[2, 4, 6, 8, 7, 5, 9, 6, 32, 2, 3, 4,  6, 78])

# Не используется. Создан для сравнения расхода памяти
numbers_list = [2, 4, 6, 8, 7, 5, 9, 6, 32, 2, 3, 4,  6, 78]

# Не используется. Создан для сравнения расхода памяти
numbers_set = {2, 4, 6, 8, 7, 5, 9, 6, 32, 2, 3, 4,  6, 78}

# Не используется. Создан для сравнения расхода памяти
numbers_tuple = (2, 4, 6, 8, 7, 5, 9, 6, 32, 2, 3, 4,  6, 78)

numbers_index = array('i')


for i in range(len(numbers)):
    if numbers[i] % 2 == 0:
        numbers_index.append(i)

result = ' '.join(map(str, numbers_index))
print(result)

show_size(i)
show_size(result)
show_size(numbers)
show_size(numbers_index)
show_size(numbers_list)
show_size(numbers_set)
show_size(numbers_tuple)


# 0 1 2 3 7 8 9 11 12 13
#  type = <class 'int'>, size = 28, object = 13, ref_count = 16
#  type = <class 'str'>, size = 71, object = 0 1 2 3 7 8 9 11 12 13, ref_count = 5
#  type = <class 'array.array'>, size = 120, object = array('i', [2, 4, 6, 8, 7, 5, 9, 6, 32, 2, 3, 4, 6, 78]), ref_count = 4
#          type = <class 'int'>, size = 28, object = 2, ref_count = 130
#          type = <class 'int'>, size = 28, object = 4, ref_count = 79
#          type = <class 'int'>, size = 28, object = 6, ref_count = 53
#          type = <class 'int'>, size = 28, object = 8, ref_count = 75
#          type = <class 'int'>, size = 28, object = 7, ref_count = 30
#          type = <class 'int'>, size = 28, object = 5, ref_count = 45
#          type = <class 'int'>, size = 28, object = 9, ref_count = 26
#          type = <class 'int'>, size = 28, object = 6, ref_count = 53
#          type = <class 'int'>, size = 28, object = 32, ref_count = 28
#          type = <class 'int'>, size = 28, object = 2, ref_count = 130
#          type = <class 'int'>, size = 28, object = 3, ref_count = 63
#          type = <class 'int'>, size = 28, object = 4, ref_count = 79
#          type = <class 'int'>, size = 28, object = 6, ref_count = 53
#          type = <class 'int'>, size = 28, object = 78, ref_count = 20
#  type = <class 'array.array'>, size = 128, object = array('i', [0, 1, 2, 3, 7, 8, 9, 11, 12, 13]), ref_count = 4
#          type = <class 'int'>, size = 24, object = 0, ref_count = 511
#          type = <class 'int'>, size = 28, object = 1, ref_count = 842
#          type = <class 'int'>, size = 28, object = 2, ref_count = 130
#          type = <class 'int'>, size = 28, object = 3, ref_count = 63
#          type = <class 'int'>, size = 28, object = 7, ref_count = 30
#          type = <class 'int'>, size = 28, object = 8, ref_count = 75
#          type = <class 'int'>, size = 28, object = 9, ref_count = 26
#          type = <class 'int'>, size = 28, object = 11, ref_count = 19
#          type = <class 'int'>, size = 28, object = 12, ref_count = 14
#          type = <class 'int'>, size = 28, object = 13, ref_count = 17
#  type = <class 'list'>, size = 176, object = [2, 4, 6, 8, 7, 5, 9, 6, 32, 2, 3, 4, 6, 78], ref_count = 4
#          type = <class 'int'>, size = 28, object = 2, ref_count = 130
#          type = <class 'int'>, size = 28, object = 4, ref_count = 79
#          type = <class 'int'>, size = 28, object = 6, ref_count = 53
#          type = <class 'int'>, size = 28, object = 8, ref_count = 75
#          type = <class 'int'>, size = 28, object = 7, ref_count = 30
#          type = <class 'int'>, size = 28, object = 5, ref_count = 45
#          type = <class 'int'>, size = 28, object = 9, ref_count = 26
#          type = <class 'int'>, size = 28, object = 6, ref_count = 53
#          type = <class 'int'>, size = 28, object = 32, ref_count = 28
#          type = <class 'int'>, size = 28, object = 2, ref_count = 130
#          type = <class 'int'>, size = 28, object = 3, ref_count = 63
#          type = <class 'int'>, size = 28, object = 4, ref_count = 79
#          type = <class 'int'>, size = 28, object = 6, ref_count = 53
#          type = <class 'int'>, size = 28, object = 78, ref_count = 20
#  type = <class 'set'>, size = 736, object = {32, 2, 3, 4, 5, 6, 7, 8, 9, 78}, ref_count = 4
#          type = <class 'int'>, size = 28, object = 32, ref_count = 28
#          type = <class 'int'>, size = 28, object = 2, ref_count = 130
#          type = <class 'int'>, size = 28, object = 3, ref_count = 63
#          type = <class 'int'>, size = 28, object = 4, ref_count = 79
#          type = <class 'int'>, size = 28, object = 5, ref_count = 45
#          type = <class 'int'>, size = 28, object = 6, ref_count = 53
#          type = <class 'int'>, size = 28, object = 7, ref_count = 30
#          type = <class 'int'>, size = 28, object = 8, ref_count = 75
#          type = <class 'int'>, size = 28, object = 9, ref_count = 26
#          type = <class 'int'>, size = 28, object = 78, ref_count = 20
#  type = <class 'tuple'>, size = 160, object = (2, 4, 6, 8, 7, 5, 9, 6, 32, 2, 3, 4, 6, 78), ref_count = 5
        #  type = <class 'int'>, size = 28, object = 2, ref_count = 130
        #  type = <class 'int'>, size = 28, object = 4, ref_count = 79
        #  type = <class 'int'>, size = 28, object = 6, ref_count = 53
        #  type = <class 'int'>, size = 28, object = 8, ref_count = 75
        #  type = <class 'int'>, size = 28, object = 7, ref_count = 30
        #  type = <class 'int'>, size = 28, object = 5, ref_count = 45
        #  type = <class 'int'>, size = 28, object = 9, ref_count = 26
        #  type = <class 'int'>, size = 28, object = 6, ref_count = 53
        #  type = <class 'int'>, size = 28, object = 32, ref_count = 28
        #  type = <class 'int'>, size = 28, object = 2, ref_count = 130
        #  type = <class 'int'>, size = 28, object = 3, ref_count = 63
        #  type = <class 'int'>, size = 28, object = 4, ref_count = 79
        #  type = <class 'int'>, size = 28, object = 6, ref_count = 53
        #  type = <class 'int'>, size = 28, object = 78, ref_count = 20

# Вывод: в принципе в задаче используется массив и он съедает минимальное кол-во памяти из всех возможных вариантов.
