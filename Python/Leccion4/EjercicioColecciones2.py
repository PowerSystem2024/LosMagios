# Ejercicio 2: Operaciones de conjuntos con listas
# Escriba un programa que tenga dos listas y q a continuacion cree las siguientes listas (En las que no debe haber repeticion)
# 1 Lista de palabras que aparecen en las listas
# 2 Lista de palabras que aparecen en la primera lista, pero no en la segunda
# 3 Lista de palabras que aparecen en la segunda lista pero no en la primera
# 4 Lista de palabras que aparecen en ambas listas

lista1 = ['hola', 'hola', 'todo', 'como', 'esta', 'todo', 'por', 'ahi']
lista2 = ['hola', 'como', 'las', 'cosas', 'estan', 'las', 'cosas', 'por', 'tu', 'casa']

# Elmiinar los elementos repetidos de ambas listas con conjuntos
conjunto1 = set(lista1)
conjunto2 = set(lista2)

lista3 = list(conjunto1 | conjunto2) # unimos los dos conjuntos

lista4 = list(conjunto1 - conjunto2)  # Lista de palabras que aparecen en la primera lista, pero no en la segunda

lista5 = list(conjunto2 - conjunto1) # Lista de palabras que aparecen en la segunda lista pero no en la primera

lista6 = list(conjunto1 & conjunto2) # Lista de palabras que aparecen en ambas listas

print(f'Lista de palabras que aparecen en las listas: {lista3}')
print(f'Lista de palabras que aparecen en la primera lista, pero no en la segunda: {lista4}')
print(f'Lista de palabras que aparecen en la segunda lista pero no en la primera: {lista5}')
print(f'Lista de palabras que aparecen en ambas listas: {lista6}')

