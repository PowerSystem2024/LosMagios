class Persona: #Esta clase hereda de la clase Object
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self, edad):
        self._edad = edad

    def __str__(self): #Override = sobreescribir
        return f"Persona:  [ Nombre: {self._nombre}, Edad: {self._edad}]"

class Empleado(Persona): #Esta clase es hija de la clase persona
    def __init__(self,nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self._sueldo = sueldo

    @property
    def sueldo(self):
        return self._sueldo
    @sueldo.setter
    def sueldo(self, sueldo):
        self._sueldo = sueldo

    def __str__(self):
        return f"Empleado: [ Sueldo: {self._sueldo}] {super().__str__()}"

empleado1 = Empleado("Gonzalo", 23, 75000)
print(empleado1.nombre)
print(empleado1.edad)
print(empleado1.sueldo)

#Tarea: encapsular los atributos y agregar los metodos getters and setters
#Crear otro objeto, pasar los datos para nombre, edad y sueldo
#Mostrar estos datos, luego modificar y mostrar nuevamente

empleado2 = Empleado("Juan", 52, 22222222)
empleado2.nombre = "Juan"
empleado2.edad = 52
empleado2.sueldo = 22222222
print(empleado2.nombre)
print(empleado2.edad)
print(empleado2.sueldo)