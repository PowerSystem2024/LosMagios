# Ejercicio 1: Eliminar duplicados de la lista
# Escriba un programa donde tenga una lista y que a continuacion elimine los elementos repeditos, por ultimo mostrar la lista

# Creamos una lista
lista = [1, 2, 3, 'Ariadna', 7, 7, 3, 'Ariel', 5, 'Ariadna', 'Ariel']
# conjunto = set(lista) # Convertimos la lista a un conjunto tipo set
# lista = list(conjunto) # Convertimos al conjunto en una lista
# Podemos hacer lo mismo en una sola linea
lista = list(set(lista))

print(lista)
