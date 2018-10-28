x = input ("Введите первую букву: ")
y = input ("Введите вторую букву: ")

pos_simbol_start = ord(x) - 96
pos_simbol_end = ord(y) - 96
simbols_between = pos_simbol_end - pos_simbol_start

print("Позиция первой буквы: ", pos_simbol_start)
print("Позиция второй буквы: ", pos_simbol_end)
print("Между ними букв: ", simbols_between)
