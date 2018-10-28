# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
#
# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=ex_05.xml#R1VdLj5swEP41XCvAvHpNNrs9tNJKObQ9RU6YBVqDkXFe%2FfUdbBMgkC6rjbJpDmT8ecbMfPOIY5F5fngStEy%2F8RiY5drxwSIPlus6ThTgV40cNRKGRAOJyGKj1ALL7A8Y0DboNouh6ilKzpnMyj644UUBG9nDqBB831d74az%2F1pImMACWG8qG6PcslqlGIzds8S%2BQJWnzZif4rHfWdPM7EXxbmPdZLnlRH72d0%2BYsE2iV0pjvOxBZWGQuOJdayg9zYDW3DW3a7vHC7slvAYWcYtD4saNsC43LyjF5bMiAGLkxSy5kyhNeULZo0ZkKGOojbVylMmcoOij%2BAimPJr10KzlC7QlfOS%2BN3tBtE0nFt2Jj%2FDCeSSoSaLR8jdUuduxMrE%2FAc5DiiAoCGJXZrp9eaqokOem1TKFgyLpA3ATeGMN6rfnZp5mEZUlVJHtsmT5LF6PfgZBw%2BGdgZteNTCJNw3lmuW%2Br12lynXYqt8HeRcUULu6khrxhDX1YCXkjtAUMvZrF2Q7FRKqohhAyNHMtDDqaqWeokEjJjpI1%2FqhkXz3RG1sJWvlBPe2Oud%2FBI2Nu3o2BjHg0jnagklerKsvXnK0qJFxaLjoR0Lyu%2FmJdlR2rtRgxAhyiU0y0erVag9wDFEOFSx6f1Wi%2FAm%2Ffsw6Z2LThFZrWIXfRtMieOP6o7T%2F5zfKnOW5SQ%2FvDhg6u3dDG9Jln6MgpfcTvpy%2B0z9KifTJWZ5k5uTEpWf4wV70ZoGV8LtTTe71nGqQqafGufu30VvesV86f2tpvOP3CFBhYntU4XsDKWsQyo4wB44mgee0siAwzBOJ877nduMWMCPtFdvrB7s4Ib2RGBFeYEcF933GIc8tLjjOBjDu55DgjQ9H7qFuOc3l4DccWproeC%2Fbxv%2BvTs9qMJpYmeXtp4rL9f6h%2FTNo%2F4WTxFw%3D%3D

x = input ("Введите первую букву: ")
y = input ("Введите вторую букву: ")

pos_simbol_start = ord(x) - 96
pos_simbol_end = ord(y) - 96
simbols_between = pos_simbol_end - pos_simbol_start

print("Позиция первой буквы: ", pos_simbol_start)
print("Позиция второй буквы: ", pos_simbol_end)
print("Между ними букв: ", simbols_between)
