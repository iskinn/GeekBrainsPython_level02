# Написать программу, которая генерирует в указанных пользователем границах:
# случайное целое число;
# случайное вещественное число;
# случайный символ. Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
#
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=ex_04.xml#R7ZlLj5swEIB%2FDdL2suIVINek6fbQSivtoe2p8oIDbo2NjPPqr68BO4TYdOk2glI1B2LGNp4Zf56xwfLW%2BfGBgSL7SBOILddOjpb31nJdx4kC8VdJTo0kDL1GkDKUyEat4An9gFJoS%2BkOJbDsNOSUYo6KrjCmhMCYd2SAMXroNttS3B21ACnUBE8xwLr0E0p41kgjN2zl7yFKMzWyEyybmmcQf08Z3RE5nuV62%2FrXVOdAPUsaWmYgoYcLkbexvDWjlDel%2FLiGuPKtclvT711P7VlvBgkf0sH1mx57gHdQqVwrxk%2FKGTARvpG3lPGMppQAvGmlq9pgWD3SFncZz7EoOqL4DXJ%2BktMLdpwKUfuED5QWsp2utrSkpDsWSz2kZhywFMpWkqpKw4tu0tQHSHPI2Uk0YBADjvbd2QUSkvTcrnWUKEhf9fhtgNswFrhW7jlkiMOnAtSGHMSK6Tqp1%2Fg9ZBwef2mYrHUjyZNcbwqvQwuvo2TZBbhK9keuWMwHIU9HyJ8KIU93m7B9dXnd1Fe%2Fnmd3XU%2FvtWdFACmqojAcYAwxTRnIhTsKyJBQCbLruse2YgIwo4Fg%2BrcAM5gPmL4O5mIqME0pIcBCq1WC9qKYVkUiWtSVNgMkofl99YcIv1OkvlGdxHAX%2FbQZ6Pp3fCKdYEwkw%2FkgudCRDKZC0pBiZJR0rGhljJhk7qHyDNwoYEbzATPQwQynAtOUYpqwVxaAnIPekMR%2BjpadnjOH2Bu6E70JxMv5QBzqEKvD7%2FgUm7KSlvHz64y%2FI2hLWT67jO%2FbIzLpzOiAvTQw6UzFpGkt%2F4%2BsLcWLMfetnj0filUYvcR4ORXFjslx%2FRj37mbzf5Rif8wXAs6MTl8q8HaCsTsZxo7Bc9oOwSAqUf5M8ddSmMHV%2FkHHn7Kkh%2B%2B7Y%2B%2Buom8sSJJXjdS%2Ffxn%2B8qNrbpV%2BWqV%2B15B%2BI%2BKM9RlBXhjlb9uaLbrhIDAdFyJDOIhucVwwvIGdIBwI77HT56r%2F%2FULdfpGPGxYqXEOouPmXEdn1kQrO2wn0ryYwDK8mplFK9rqam7Maw2KQq0%2FXS2lTraR5J8nQGzNJDlkVE37aioae3l7xbUvctp9eG0Tb79ve5ic%3D

import random

x = int(input ("Введите начало диапазона для целого числа: "))
y = int(input ("Введите конец диапазона для целого числа: "))
n = random.randint(x, y)
print("Случайное целое число из диапазона = ", n)

x = int(input ("Введите начало диапазона для вещественного числа: "))
y = int(input ("Введите конец диапазона для вещественного числа: "))
m = random.uniform(x, y)
print("Случайное вещественное число из диапазона = ", m)

x = input ("Введите симвод начало диапазона: ")
y = input ("Введите символ конец диапазона: ")
simbol_start = ord(x)
simbol_end = ord(y)
n = random.randint(simbol_start, simbol_end)
simbol = chr(n)
print("Случайный символ = ", simbol)
