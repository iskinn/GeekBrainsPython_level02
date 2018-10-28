# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=ex_07.xml#R5VpJc5swFP41PjYDiMU%2Bxo6THtqZzOTQ9iiDAjQCMbK89ddXgGQQiJQkGDuuD1g8bU%2Ff22VPwCLZP1CYRd9JgPDEMoL9BNxNLMs0py7%2FyimHkuJ5oCSENA7EoIrwFP9BgmgI6iYO0FoZyAjBLM5Uok%2FSFPlMoUFKyU4d9kywumsGQ9QiPPkQt6k%2F4oBFJXVqeRX9K4rDSO5surOyZwX9l5CSTSr2m1jgufiU3QmUa4mDriMYkF2NBJYTsKCEsLKV7BcI59hK2Mp59x29R74pSlmfCZKPLcQbJFkuGGMHCQYKODbilVAWkZCkEC8r6rw4MMqXNPhbxBLMmyZv%2FkaMHYR44YYRTqpW%2BEZIJsa12RYnWZMN9QUfgjMGaYjkKKek5SzW5omzPiCSIEYPfABFGLJ4q4oXCi0Jj%2BMqpHhDgNUBXA%2FcMOb6muOzi2KGnjJYnGTHTUZFqfP0W0QZ2r96MNFrTYUghcHZ4nVXaa8pZR3VNFfSPgKFe9lQOMaIWFj257EnaTx1g7LAuQxKclNHjh9%2FXn8ui6ed7zSxFrm7Lb%2F8Fsbcr2Z5k0MAMUaYhBQmHJgM0Zizhmiz77HqOIOOTnuqqD2Aitp9XNfpVZSDRw8%2F8%2Fk3jnz9JZbrFw5AW30lPsOpr5j6SGLOylF%2B9tRR5HdMXOQSJVNiVkM2Rzb6iUtjF1cjrsG9jV5c5mw0ccljKuJyMT%2FwPIi3vBnmTe6%2BOAcuTHLXUnSWzqxN9I%2BUdLXOCpor%2Bu5rC2r2kKR1BlNJI7Q2vd7x7l383ieBXWs2lJlGJFlt1uP4YU9VDNPROGKgccTmEMkC0CQLeYC7K57OhJ9y2jZ2fjSmArFmlLygBcEkD2spSXOLf44xbpAgjsOUv%2FocsCLQ5UDFvOq5FR1JHAS4K0tTXcgQ4BtqEDQ1UdA%2BUZ4GOrINu3ga1wu6Dc4HunMloUziUw9l7liJhyo%2BMOsXyW4phYfasCwfsO6%2Fj%2B017hEa44H96njeKDl4dxakuacQdQF3knNtjbBqKdeFVwW2pYJoeWOWBbOLM05nWjfPL8aNcbTXmmDeYLe6FHQkwwW2mmmApswGMlwALO0%2BQxmiY16cmrzPh%2Bt0wRtHF5xxVMHTbzOYS%2B5V6XSVAldS6XQVchdX6ZigUQLrrpxOVuk47jmcRD9HMFoA6LiWHjoANDMx542ZmzOwm9D8PPCvzA22tOXCMzfLVa3L7vubwxCZG0%2BTLta4vHaUPY29fTA4nr2%2B8d5uJZ%2FuVw%2FznEZi6QG%2B%2BgufVhpotlE%2F2YWPJkX8jy44Z8ZYyPPX6j8jpfup%2FpgDln8B

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
