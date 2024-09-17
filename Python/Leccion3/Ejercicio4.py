calificacionBaja = 1000000
suma = 0
contador = 0

while contador < 10:
    calificacion = int(input('Digite una calificacion: '))
    suma += calificacion
    if calificacion < calificacionBaja:
        calificacionBaja = calificacion
    contador += 1

calificacionPromedio = suma / 10

print(f'La calificacion ms baja es: {calificacionBaja}. Y la calificacion promedio es: {calificacionPromedio}')

