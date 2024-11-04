from Empleado import Empleado
from Gerente import Gerente


def imprimir_detalles(objeto):
    #print(objeto)  # De manera indirecta llama al str de la clase Empleado o Gerente
    print(type(objeto))  # Esto es para saber el tipo de dato que recibe
    print(objeto.mostrar_detalles())
    if isinstance(objeto, Gerente):
        print(objeto.departamento)

empleado = Empleado('Pablo', 80000.00)
imprimir_detalles(empleado)

gerente = Gerente('Rodrigo', 60000.00, 'Producción')
imprimir_detalles(gerente)
