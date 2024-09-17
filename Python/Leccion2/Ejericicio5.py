# Ejercicio 5
# Sistema de Calificaciones
num = int(input('Ingrese un valor del 1 al 10: '))

if num == 9 or num == 10:
    print('Calificacion: A')
elif num == 8:
    print('Calificacion : B')
elif num == 7:
    print('Calificacion : C')
elif num == 6:
    print('Calificacion : D')
elif 0 <= num < 6:
    print('Calificacion: F')
else:
    print('El valor ingresado es incorrecto')

