numPositivos = 0
numNegativos = 0
numNeutros = 0
i = 1
while i <= 10:
    num = int(input('Digite un numero: '))
    if num > 0:
        numPositivos += 1
    elif num < 0:
        numNegativos += 1
    else:
        numNeutros += 1
    i += 1

print(f'La cantidad de numeros positivos es: {numPositivos}. La cantidad de numeros negativos es: {numNegativos} y la cantidad de numeros neutros es: {numNeutros}')