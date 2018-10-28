a = int(input ("Введите первое число: "))
b = int(input ("Введите второе число: "))
c = int(input ("Введите третье число: "))

if a < b < c or c < b < a:
    x = b
elif b < a < c or c < a < b:
    x = b
else:
    x = c

print("Среднее число = ", x)
