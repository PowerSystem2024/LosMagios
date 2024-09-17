
i = 1
suma = 0

while i <= 5:
    print(f'Salario del empleado {i}')
    horas = int(input('Digite la cantidad de horas trabajadas: '))
    tarifa = int(input('Digite la tarifa por hora: '))
    salario = horas * tarifa
    print(f'El salario es: ${salario}')
    suma += salario
    i += 1
    print('')

print(f'La suma de los salarios es: ${suma}')
