# Посчитать четные и нечетные цифры введенного натурального числа. 
# Например, если введено число 34560, то у него 3 четные 
# цифры (4, 6 и 0) и 2 нечетные (3 и 5). 


x = input('Введите число: ')
count_nech = 0
count_ch = 0

for i in x:
    if int(i) % 2 == 1:
        count_nech += 1
    else:
        count_ch += 1

print(f'Четных чисел: {count_ch}.Нечетных чисел: {count_nech}')
