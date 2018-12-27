# 1. Определение количества различных подстрок с использованием хеш-функции. 
# Пусть дана строка S длиной N. Например, состоящая только из маленьких латинских букв. 
# Требуется найти количество различных подстрок в этой строке. 
# Для решения задачи рекомендую воспользоваться алгоритмом sha1 
# из модуля hashlib или встроенную функцию hash()

import hashlib


# Сама строка для перебора
str_ = 'poodooi'

# Сначала иницициализируем список, для заполнения хешами.
# Первый цикл задает длину n строковых последовательностей.
# Второй цикл for нужен для перебора и сравнения строковых последовательностей длиной n символов.
def check_hash(str_):
    hash_ = []
    for n in range(len(str_)):
        for i in range((len(str_)) - n + 1):
            j = i + n
            spam = str_[i:j]
            hash_sha1 = hashlib.sha1(spam.encode('utf-8')).hexdigest()
            if hash_.count(hash_sha1) == 0:
                hash_.append(hash_sha1)
# Отладочные выводы промежуточных данных
#                print(hash_sha1)
#                print('spam:', spam)
    return len(hash_)

print('Кол-во подстановок:', check_hash(str_))
