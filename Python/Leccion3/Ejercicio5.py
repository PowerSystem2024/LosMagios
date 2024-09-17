num = 0
i = 1
factorial = 1

while num <= 0:
    num = int(input('Digite un numero: '))

while i <= num:
    factorial *= i
    i += 1

print(f'El factorial es: {factorial}')
