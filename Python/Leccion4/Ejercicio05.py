# Ejercicio 5: Factorial de un numero positivo
#Hacer un programa para calcular el factorial de un numero positivo
numero = int(input('Digite un numero: '))
while numero < 0:
    print('Error -> el numero tiene que ser positvo')
    numero = int(input('Digite un numero: '))
factorial = 1 # Variable para calcular el factorial
for i in range(1, numero+1):
    factorial *= i
print(f'\n El factorial del numero {numero} positivo ingresado es de : {factorial}')
