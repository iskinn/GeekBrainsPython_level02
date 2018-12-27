from collections import namedtuple

# Функция подсчета годового дохода.
# Пока чтоне нашел как уйти от eval. Но думаю есть способ.
def profit_sum_calculate(name):
    sum_profit_string = name + '.profit_01' + '+' + name + '.profit_02' + '+' + name + '.profit_03' + '+' + name + '.profit_04'
    sum_profit = eval(sum_profit_string)
    return sum_profit

# Функция подсчета среднего годового дохода.
def profit_avg_calculate(list_):
    sum_profit = 0
    for name in list_:
        sum_profit += profit_sum_calculate(name)
    sum_profit_avg = sum_profit / len(list_)
    return sum_profit_avg

organization = namedtuple('organization', ['name', 'profit_01', 'profit_02', 'profit_03', 'profit_04'])

# Вместо ручного ввода использовал заранее предопределенные организации
teatr = organization('Teatr', 100, 200, 300, 150)
taxi = organization('Taxi', 110, 400, 260, 201)
radio = organization('Radio', 200, 110, 380, 0)
kiosk = organization('kiosk', 210, 270, 470, 50)
shop = organization('Shop', 315, 410, 130, 370)

# Список всех организаций
organizations = ['teatr', 'taxi', 'radio', 'kiosk', 'shop']

# Вычисляем средний доход
profit_avg = profit_avg_calculate(organizations)

# Формируем списки по доходу каждой организации
list_lower_avg = []
list_above_avg = []
for name in organizations:
    if profit_sum_calculate(name) < profit_avg:
        list_lower_avg.append(name)
    else:
        list_above_avg.append(name)

# Выводим списки
print('Организации с доходом ниже среднего:', list_lower_avg)
print('Организации с доходом выше среднего:', list_above_avg)
