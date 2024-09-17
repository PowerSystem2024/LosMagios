# Ejercicio 3: Agregar eprsonajes a una lista
# Escriba un programa donde cree una lista con los siguientes persoajes del señor de los anillos
# Nombre: Aragon
# Clase: Guerrero
# Raza: Dúnadan del norte

#Nombre: Gandalf
#Clase: Mago
#Raza: Instar

#Nombre: Legolas
#Clase: Arquero
#Raza: Elfo sindar

personajes = [] # Creamos una lista vacia
# Creamos diccionarios
P = {'Nombre' : 'Aragon', 'Clase' : 'Guerrero', 'Raza' : 'Dúnadan del norte'}
personajes.append(P) # Agregamos el diccionario a la lsta
P = {'Nombre' : 'Gandalf', 'Clase' : 'Mago', 'Raza' : 'Instar'}
personajes.append(P)
P = {'Nombre' : 'Legolas', 'Clase' : 'Arquero', 'Raza' : 'Elfo Sindar'}
personajes.append(P)
print(personajes)