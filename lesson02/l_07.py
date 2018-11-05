# Написать программу, доказывающую или проверяющую, 
# что для множества натуральных чисел выполняется равенство: 
# 1+2+...+n = n(n+1)/2, где n – любое натуральное число.

n = int(input('Введите число: '))
Sum_left = 1

for i in range(n):
    Sum_left += i

Sum_right = (n*(n + 1))/2

if Sum_left == Sum_right:
    print('Равенство верно')
else:
    print('Равенство неверно')

print (f'Sum_left {Sum_left}. Sum_right {Sum_right}')
