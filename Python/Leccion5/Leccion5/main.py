# Comenzamos con funciones
# mi_funcion() # No se puede llamar antes de definir una funcion
# Definimos una funcion
def mi_funcion(): # Para identificar a la funcion utilizamos parentesis
    print("Saludos a todos los alumnos de la Tecnicatura")

mi_funcion() # Estamos llamando a la funcion
mi_funcion() # Se puede llamar a una funcion N cantidad de veces

#Desempaquetado de listas o list Unpacking
def show(name, lastName):
    print(name+" "+lastName)
person = ["Gonzalo", "Bucca"]
show(person[0], person[1]) #Pasamos uno por uno los datos de la lista a la funcion
show(*person) #Esto es lo mismo que lo anterior pero le pasamos todo junto
person2 = ("Ramiro", "Vidal") #Desempaquetamos a traves de una tupla
show(*person2)
person3 = {"lastName": "Santos", "name": "Matias"}
show(**person3)

#Repaso for else
numers = [1, 2, 3, 4, 5] #Aun con la lista vacia se va a ejecutar el else
for n in numers:
    print(n)
    if n == 3:
        break #Esta es la unica manera para que no se ejecute el else
else:
    print("Esto se termino")

#List comprehension, lista de comprension
names = ["Paolo", "Rodrigo", "Lupe", "Pepe"]
alongP = [p for p in names if p[0] == "P"] #Esto regresa una nueva lista
print(alongP)

bottleC = [{"name":"Quilmes", "country": "Arg"},
           {"name":"Corona", "country": "Mx"},
           {"name":"Stella Artois", "country": "Belgium"},
           ]
Arg = [b for b in bottleC if b ["country"] == "Arg"]
print(Arg)
print(bottleC)

#Paso de argumentos (funciones)
def mi_funcion2(name, lastName):
    print("Saludos a todos los que nos ven a traves del canal de YouTube")
    print(f"Nombre: {name}, Apellido: {lastName}")
mi_funcion2("Jorge", "Lucero")
mi_funcion2("Gonzalo", "Bucca")
mi_funcion2("Juan Carlos", "Bucca")

