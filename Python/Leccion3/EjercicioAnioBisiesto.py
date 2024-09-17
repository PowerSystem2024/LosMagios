opcion = 1
while opcion == 1:
    numero = int(input('Por favor ingrese un año: '))
    if (numero % 4 == 0) and (numero % 100 != 0) or (numero % 400 == 0):
        print('El año es bisiesto')
    else:
        print('El año no es bisiesto')

    opcion = int(input('Para continuar digite la opcion 1: '))
