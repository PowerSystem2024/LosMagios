# Ejerciciol 3: Insertar elementos y ordenarlos
# Pedir numeros y meterlos en una lista, cuando el usuario introduzca un numero 0 , nuestro programa deja de insertar
# Por ultimo mostrar los numeros ordenados de menor a mayor
lista = []
salir = False
while not salir:
    numero = int(input('Digite un numero: '))
    if numero == 0:
        salir = True
    else:
        lista.append(numero)
lista.sort() # La lista se ordena con esta funcion
print(f'\n Lista ordenada: \n{lista}')