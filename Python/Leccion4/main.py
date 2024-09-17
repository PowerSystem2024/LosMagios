## COLECCIONES EN PYTHON
from typing import Dict

# LISTAS - En otros lenguajes se las conoce como arreglos

nombres = ['Ariadna', 'Flavia', 'Rodrigo', 'Mario']
print(nombres)
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])


# Si no sabemos en que numero esta el ultimo elemento, para q nos muestre el ultimo elemento ponemos: -1
# Para ir del ultimo hacia el primero arrancamos con -1
# Ejemplo:

print(nombres[-1])
print(nombres[-2])
print(nombres[-3])


# A continuacion en el primer lugar del corchete indicamos desde que indice nos va a mostrar
# y en el segundo va la cantidad de elementos desde ese indice (incluyendolo)

print(nombres[0:2])

#Ahora vamos desde el inicio
print(nombres[ :3])

#Desde el indice indicado hasta el final
print(nombres[1: ])

# Modificamos un valor
nombres[2] = 'Rodri'
nombres[0] = 'Ari'
print(nombres)


# Iterar una lista
for nombre in nombres: #Nombre es singular, la lista es plural
    print(nombre)
else:
    print('Se acabaron los elementos de la lista')


# Preguntamos cuantos elementos tiene una lista con la funcion LEN y como parametro le pasamos la lista
print(len(nombres))



# Agregamos un elemento al final de la lista
nombres.append('Cucha')
print(nombres)
# En una lista puede haber diferentes tipos de datos - tambien dentro de una lista puede haber otra lista
nombres.append([2, 3, 6, 4])
nombres.append(True) #boolean
nombres.append(10.45) # float
print(nombres)

#Insertar un elemento en un indice especifico
nombres.insert(2, 'Lupita')
print(nombres)


# Eliminamos un nombre con el valor

nombres.remove('Lupita')
print(nombres)

# Eliminar el ultimo elemento de la lista
nombres.pop()
print(nombres)


# Eliminar un indice especifico con del (delete)
del nombres[2]
print(nombres)

#Eliminar o borrar todos los elementos. o limpiar toda la lista
nombres.clear()
print(nombres)

#Eliminar la lista
del nombres
# print(nombres)  Aqui nos mostrara un error pq la lista ya no existe

# IMPORTANTE: Las listas son 'mutables' o 'modificables'
# La tupla es similar a la lista pero es 'inmutable' ya que sus elementos no se pueden elimina
# Esta es la gran diferencia entre lista y tupla

# Definimos una tupla
cocina = ('cuchara', 'tenedor', 'cuchullo')
print(cocina)

# Para saber la cantidad de elementos q hay en una tupla
print(len(cocina))

# Acceder a un elemento, para esto utilizamos corchetes no parentesis
print(cocina[0])

# Mostrar de manera inversa, de atras hacia adelante
print(cocina[-1]) # ultimo elemento

# Acceder a un rango
print(cocina[0:1]) # Aca nos va a mostrar el primer elemento

# Ejemplo
# Una tupla necesita aunque sea un solo elemento una coma si o si
verduras = ('papa',) # Si no tiene lo toma como string, pero si le ponemos una coma se convierte en tupla
print(verduras)

# Recorremos los elementos de la tupla
for cocinar in cocina: # print esta usando \n para saltos de linea
    print(cocinar, end=' ') # usamos end= para eliminar los saltos de linea


# La unica forma de agregar un elemento a una tupla es
# convirtiendo la tupla en lista y desp de nuevo a tupla. ESTO NO ES UNA BUENA PRACTICA
# Ejemplo:

listaCocina = list(cocina)
listaCocina[0] = 'Plato'
cocina = tuple(listaCocina)
print('\n', cocina)

# Para eliminar una tupla
del cocina
# print(cocina)

###########################################################
###########################################################
#########CLASE 2 - COLECCIONES PARTE 2#####################
###########################################################
###########################################################

# Tipo set - Coleccion desordenada de elementos unicos q no se repiten
planetas = {'marte', 'jupiter', 'venus'}
print(planetas)

# len nos muestra la cantidad de elementos q tiene el set
print(len(planetas))

# Revisar si un elemento existe dentro de set
print('marte' in planetas) # devuelve true o false

#Agregar un elemento
planetas.add('saturno')
print(planetas)

# Eliminar elementos - puede arrojar error si el elemento no existe
planetas.remove('venus')
print(planetas)
# con discard tambien eliminamos elementos pero este NO tira error si el elemento no existe
planetas.discard('tierra')
print(planetas)

# Limpiar set
planetas.clear()
print(planetas)

#Eliminar set
del planetas


# DICCIONARIO - un diccionario esta compuesto por dos elementos: key - value
diccionario = {
    'IDE':'Integrated Development Environent',
    'POO':'Programacion orientada a objetos',
    'SABD':'Sistema de administracion de base de datos'
}

print(diccionario)
#Largo del diccionario
print(len(diccionario))

# Acceder a un diccionario con la key
print(diccionario['IDE'])

# Otra forma de obtener un elemento
print(diccionario.get('POO'))

# Modificamos elementos
diccionario['IDE'] = 'Entorno de desarrollo integrado'

print(diccionario)

# Como recorrer elementos
for termino in diccionario:
    print(termino) # Esto nos muestra solo las LLAVES (KEYS)

# Necesitamos una funcion para recorrer un diccionario y que nos muestre tambien el VALOR
for termino, valor in diccionario.items():
    print(termino, valor)

# Otras maneras de acceder al diccionario - Solo muestra las llaves con una funcion
for termino in diccionario.keys():
    print(termino)

# Para obtener solo el valor sin las llaves:
for valor in diccionario.values():
    print(valor)

# Comprobar la existencia de un elemento - nos devuelve true o false
print('IDE' in diccionario)

# Agregar un elemento al diccionario
diccionario['PK'] = 'Primary Key'
print(diccionario)

# Eliminar un elemento
diccionario.pop('POO')
print(diccionario)

#Vaciar un diccionaro
diccionario.clear()
print(diccionario)

# Eliminar diccionario
del diccionario

# Concatenamos listas
lista1 = [1, 2, 3, 4]
lista2 = [4, 6, 7, 8]
lista3 = lista1+lista2
print(lista3)

#Extend - funcion para agregar varios elementos a una lista
lista3.extend([9, 10, 11])
print(lista3)

# Funcion para saber en que indice esta cierto elemento - Si ponemos un valor q no est'a nos da un error
print(lista3.index(7))

# Como saber cuantos valores repetidos hay dentro de una lista
print(lista3.count(4))

# Para poner al reves una lista
lista3.reverse()
print(lista3)

#Para que una lista se multiplique repitiendo sus elementos
listaNueva = [1, 2, 3] * 2
print(listaNueva)

#Metodos de ordenamiento
listaNueva.sort() #Los ordena ascendentemente
print(listaNueva)
listaNueva.sort(reverse=True) # Descendente
print(listaNueva)

tuplaNueva = (4, 'Hola', 8.45, [1, 2, 3], 4, 'Hola') # Puede tener diferentes tipos de datos
print(tuplaNueva)
print(4 in tuplaNueva) #Accion booleana para saber si esta el elemento


############################################################################
#########################CLASE 3 - COLECCIONES PARTE 3######################
############################################################################

# SET O CONJUNTO - Para definir un conjunto:
# La unica manera de inicializar un conjunto VACIO es con SET
conjunto2 = set()
conjunto1 = {'bye'}

conjunto2.add(7)
conjunto2.add('hola')
print(conjunto2)
conjunto1.add('EL')
conjunto1.add('holaa')
print(conjunto1)
print(3 not in conjunto1)


# Operaciones en conjuntos
#unir ambos conjuntos
conjunto3 = conjunto1 | conjunto2 # La linea une ambos conjuntos
print(conjunto3)

# aca se va a guardar solo el elemento q tengan en comun
conjunto3 = conjunto1 # Noencontre el signo

# Asignar el valor que esta en el conjunto 1 y no en el conjunto2
conjunto3 = conjunto1 - conjunto2
print(conjunto3)

# Elementos que no comparten o que son diferentes entre ambos
conjunto3 = conjunto1 ^ conjunto2
print(conjunto3)

conjunto3 = conjunto1 | conjunto2
print(conjunto2.issubset(conjunto3)) # Aca preguntamos si un conjunto es un subconjunto dentro de otro
print(conjunto1.issubset(conjunto3))
print(conjunto3.issubset(conjunto1))
print(conjunto3.issubset(conjunto2))

print(conjunto3.issuperset(conjunto1)) # preguntamos si el conjunto3 tiene todos los elementos del conjunto1 - al ser true eso lo hace un SUPERCONJUNTO
print(conjunto3.issuperset(conjunto2))
print(conjunto2.issuperset(conjunto3))
print(conjunto1.issuperset(conjunto3))

# Como saber si ambos conjuntos son disconexos, esto es si no comparten elementos en comun
print(conjunto1.isdisjoint(conjunto2)) # Es verdadero q son disconexos

# Convertir un conjunto totalmente en inmutable
conjunto1 = frozenset #Esto hace q el conjunto sea totalmente inmutable
# No se puede modificar agregar ni eliminar elementos del conjunto

# Repaso de diccionarios
diccionarioNuevo = {'Azul' : 'Blue', 'Rojo' : 'Red', 'Verde' : 'Green', 'Amarillo' : 'Yellow'}
print(diccionarioNuevo)

# Como eliminar
del (diccionarioNuevo['Azul'])
print(diccionarioNuevo)

# Los diccionarios aceptar diferentes tipos de datos
diccionario2 = {'Ariel' : {'edad' : 24 , 'altura' : 1.80}, 'Ariadna' : [23, 1.50], 'Natalia' : [35, 1.67]}
print(diccionario2)

seleccionArgentina = {
    10 : {'nombre': 'Lionel Messi', 'edad' : 35, 'altura' : '1,70', 'precio' : '50 millones', 'posicion' : 'Extremo derecho'},
    11 : {'nombre': 'Angel di Maria', 'edad' : 34, 'altura' : '1,80', 'precio' : '12 millones', 'posicion' : 'Extremo derecho'},
    21 : {'nombre': 'Paulo Dybala', 'edad' : 28, 'altura' : '1,77', 'precio' : '35 millones', 'posicion' : 'Media punta'},
    19 : {'nombre': 'Nicolas otamendi', 'edad' : 34, 'altura' : '1,83', 'precio' : '35 millones', 'posicion' : 'Defensor'},
    1 : {'nombre': 'Franco Armani', 'edad' : 45, 'altura' : '1,87', 'precio' : '3.5 millones', 'posicion' : 'Portero'},
}

print(seleccionArgentina)

for llave in seleccionArgentina:
    print(llave)

for valor in seleccionArgentina.values():
   print(valor)

for llave, valor in seleccionArgentina.items():
    print(llave, valor)

 # Agregar por lo menos 4 jugadores mas en el diccionario seleccionArgentina
print('Tenemos cargados en el diccionario la cantidad de jugadores: ', end=' ')
print(len(seleccionArgentina))

# Pilas usando listas
pila = [1, 2, 3]

# Agregar elementos a la pila por el final
pila.append(4)
pila.append(5)
print(pila)

#Sacamos elementos desde el final - Eliminamos el ultimo elemento de nuestra lista y lo retorna
elementoEliminado = pila.pop()
print(f'Sacamos el elemento {elementoEliminado}')
print(f'La pila ahora quedo asi: {pila}')

# Colas con listas
# Estructura de datos tipo fifo(First Input / First Output)(primero en entrar / primero en salir)
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']

# Agregamos elementos al final de la cola
cola.append('Natalia')
cola.append('Jose')
print(cola)

# Sacamos elementos de la cola
seRetira = cola.pop(0) # Se va el elemento de la posicion 0
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)

seRetira = cola.pop(0)
print(f'Atendido el cliente: {seRetira}')
print(cola)


# Clase 4
# Seguimos mostrando como recorrer un diccionario con un ciclo for
for i in seleccionArgentina:
    print(f'{i} -> {seleccionArgentina[i]}')
