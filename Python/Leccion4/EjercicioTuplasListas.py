import math # Importamos la clase math para hacer uso de la funcion sqrt (raiz cuadrada)


# Dada la siguiente tupla
tupla = (13, 1, 8, 3, 2, 5, 8)
# Crear una lista que solo incluya los numeros menores a 5
# e imprima por consola [1, 3, 2]

lista= []
for numero in tupla:
    if numero < 5:
        lista.append(numero)

print(lista)

# Ejercicio de matematicas
# Para sacar la raiz cuadrada de un numero positivo
numero = int(input('Digite un numero positivo: '))
while numero < 0:
    print('Error -> Deberia ser un numero positivo')
    numero = int(input('Digite un numero positivo: '))
print(f'\n Su raiz cuadrada es : {math.sqrt(numero):.2f}')