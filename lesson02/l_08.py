# Посчитать, сколько раз встречается определенная цифра в 
# введенной последовательности чисел. 
# Количество вводимых чисел и цифра, 
# которую необходимо посчитать, задаются вводом с клавиатуры. 

n = input('Введите число: ')
x = input('Какое число посчитать: ')
count = 0

for i in n:
    if i == x:
        count += 1

print (f'Количество: {count}')
