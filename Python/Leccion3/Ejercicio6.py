i = 1
conteoPares = 0
conteoImpares = 0
sumaPares = 0
sumaImpares = 0

numElementos = int(input('Digite la cantidad de elementos a ingresar: '))

while i <= numElementos:
    num = int(input('Digite un elemento:'))
    if num % 2 == 0:
        conteoPares += 1
        sumaPares += num
    else:
        conteoImpares += 1
        sumaImpares += num
    i += 1

if conteoPares == 0:
    print('No se han ingresado numeros pares')
else:
    print(f'La cantidad de numeros pares es: {conteoPares}. La suma de los numeros pares es: {sumaPares}')

if conteoImpares == 0:
    print('No se han ingresado numeros pares')
else:
    promedioImpares = sumaImpares / conteoImpares
    print(f'La cantidad de numeros impares es: {conteoImpares}. La suma de los numeros pares es: {sumaImpares}')



