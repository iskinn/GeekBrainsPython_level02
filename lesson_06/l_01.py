# Написать программу, которая будет складывать, вычитать, умножать или делить два числа. 
# Числа и знак операции вводятся пользователем. 
# После выполнения вычисления программа должна не завершаться, а запрашивать новые данные для вычислений. 
# Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. 
# Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа сообщает ему об ошибке 
# и снова запрашивает знак операции. 
# Также пользователю нужно сообщать о невозможности деления на ноль, 
# если он ввел 0 в качестве делителя.

import sys, operator


# В функцию добавил вывод кол-ва ссылок: ref_count = {sys.getrefcount(x)
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

ops = {'+': operator.add,
       '-': operator.sub,
       '*': operator.mul,
       '/': operator.truediv}

x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = input('Введите знак операции: ')

if z == '0':
    sys.exit
   
if z in {'+', '-', '*', '/'}:
    if z == '/' and y == 0:
        print('Делить на 0 нельзя')
    else:
        op_func = ops[z]
        result = op_func(x, y)
        n = result
        print(result)

show_size(x)
show_size(y)
show_size(z)
show_size(ops)

# Введите первое число: 2314243
# Введите второе число: 45676
# Введите знак операции: -
# 2268567
#  type = <class 'int'>, size = 28, object = 2314243, ref_count = 4
#  type = <class 'int'>, size = 28, object = 45676, ref_count = 4
#  type = <class 'str'>, size = 50, object = -, ref_count = 14
#  type = <class 'dict'>, size = 240, object = {'+': <built-in function add>, '-': <built-in function sub>, '*': <built-in function mul>, '/': <built-in function truediv>}, ref_count = 4
#          type = <class 'str'>, size = 50, object = +, ref_count = 13
#          type = <class 'builtin_function_or_method'>, size = 72, object = <built-in function add>, ref_count = 10
#          type = <class 'str'>, size = 50, object = -, ref_count = 16
#          type = <class 'builtin_function_or_method'>, size = 72, object = <built-in function sub>, ref_count = 11
#          type = <class 'str'>, size = 50, object = *, ref_count = 15
#          type = <class 'builtin_function_or_method'>, size = 72, object = <built-in function mul>, ref_count = 10
#          type = <class 'str'>, size = 50, object = /, ref_count = 30
#          type = <class 'builtin_function_or_method'>, size = 72, object = <built-in function truediv>, ref_count = 10

# Вывод:
# В этой задаче можно добиться уменьшения расхода памяти, если убрать словарь и сделать все несколькими блоками if.