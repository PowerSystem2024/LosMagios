class Persona: #Creamos una clase
    def __init__(self, nombre, apellido, dni, edad, *args, **kwargs): #Se lo llama metodo Init Dunder
        self.nombre = nombre
        self.apellido = apellido
        self._dni = dni #Este atributo esta encapsulado de una manera sugerida
        self.edad = edad
        self.args = args
        self.kwargs = kwargs

    def mostrar_detalle(self): #self es igual a this
        print(f"La clase Persona tiene los siguentes datos: {self.nombre} {self.apellido} {self._dni} {self.edad}, la direccion es: {self.args}, los datos importantes son: {self.kwargs}")


persona1 = Persona("Gonzalo", "Bucca", 43152354, 23) #Necesitamos enviar argumentos
#print(persona1.nombre) #Hacer el print igual que la persona2
#print(persona1.apellido)
#print(persona1.edad)
print(f"El objeto1 de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")
persona2 = Persona("Ramiro", "Vidal", 34876654,  23)
print(f"El objeto2 de la clase persona: {persona2.nombre} {persona2.apellido} Su edad es: {persona2.edad} ")



persona1.nombre = "Matias"
persona1.apellido = "Santos"
persona1.edad = 23
print(f"El objeto1 modificado de la clase persona: {persona1.nombre} {persona1.apellido} Su edad es: {persona1.edad}")

#Los atributos son: caracteristicas
#Los metodos son: el comportamiento que van a tener los objetos (acciones)
persona1.mostrar_detalle() #La referencia en este caso se pasa de manera automatica
persona2.mostrar_detalle()

#Persona.mostrar_detalle(persona1) #Debemos pasarle una referencia para el self o dara error
persona1.telefono = "44445555289"
print(f"Este es el telefono de {persona1.nombre}: {persona1.telefono}") #Hemos creado un atributo de un objeto

#print(persona2.telefono) #El objeto persona2 no tiene este atributo, da error
persona3 = Persona("Rogelio", "Romero", 43524465,  22, "telefono", "2604340987", "Calle Lopez", 823, "Manzana", 77, "Casa", 18, Altura =1.83, Peso=105, CFavorito="Azul", Auto="Citroen", Modelo="2021")
persona3.mostrar_detalle()
# print(persona3._dni) esto no se debe utilizar (esta encapsulado), esto dice que lo desconocemos python
#persona3.__nombre #Esta totalmente encapsulado