"""
miVariable = 3
print(miVariable)
miVariable = "Hola a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5
print(miVariable)
y = 10
x = 2
z = x + y
print(z)
print(id(y))  # esta es la direccion de memoria. Las literales se escriben y = x296.
# La direccion de memoria va a cambiar cada vez que el programa se vuelva a ejecutar
print(id(x))

# Tipos int, float, String, Booleano
a = 10
print(a)
print(type(a))
a = 14.5
print(a)
print(type(a))
a = "Holaa"
print(a)
print(type(a))
a = True
print(a)
print(type(a))
a = False
print(a)
print(type(a))

# Manejo de cadenas (string)

miGrupoFavorito = 'Radiohead'
caracteristicas = 'Cantante: Tom yorke'
print('Mi grupo favorito es: ' + miGrupoFavorito + ' ' + caracteristicas)
miGrupoFavorito = 'Pescado Rabioso'
caracteristicas = 'Cantante: Spinetta'
print('Mi grupo favorito es:', miGrupoFavorito, caracteristicas)

numero1 = 7
numero2 = 8
print(int(numero1) + int(numero2))

# Tipos booleanos (Bool)
miBooleano = 1 > 2
print(miBooleano)

if miBooleano:
    print('El resultado es: Verdadero')
else:
    print('El resultado es falso')

# Procesar la entrada de datos
# Funcion input - Esta funcion regresa un dato tipo string
#resultado = input('Digite un numero: ')
#print(resultado)

# Conversion de la entrada de datos
#numero1 = int(input('escribe el primer numero: '))
#numero2 = int(input('escribe el segundo numero: '))
#resultado = numero1+numero2
#print('El resultado de la suma es:', resultado)


# EJERCICIO 1
notaDia = input('¿Como estuvo tu dia?(1 al 10)')
print('Mi dia estuvo un:', notaDia)

# EJERCICIO 2
titulo = input('Proporciona el titulo: ')
autor = input('Proporciona el autor: ')
print(titulo, 'fue escrito por', autor)
"""
'''
# Operadores Aritmeticos
operandoA = 8
operandoB = 5

suma = operandoA + operandoB
print(f'El resultado de la suma es: {suma}')  #Esta forma de imprimir se llama INTERPOLACION

resta = operandoA - operandoB
print(f'El resultado de la resta es {resta}')

multiplicacion = operandoA * operandoB
print(f'El resultado de la multiplicacion es: {multiplicacion}')

division = operandoA / operandoB
print(f'El resultado de la division es: {division}')

division = operandoA // operandoB  # Este operador divide y le quita el numero desp de la coma
print(f'El resultado de la division (int) es: {division}')

modulo = operandoA % operandoB
print(f'El residuo de la division es: {modulo}')

exponente = operandoA ** operandoB
print(f'El resultado de la potencia es: {exponente}')
'''
'''
# Ejercicio: RECTANGULO
alto = int(input('Proporcione el alto del rectangulo: '))
ancho = int(input('Proporcione el ancho del rectangulo: '))

area = alto * ancho
perimetro = (alto + ancho)*2

print(f'El area del rectangulo es: {area} y el perimetro es {perimetro}')
'''
'''
miVariable3 = 10
print(miVariable3)

# Operador de reasignacion
miVariable3 = miVariable3 + 1
print(miVariable3)
miVariable3 += 1
print(miVariable3)

#miVariable3 = miVariable3 - 2
miVariable3 -= 2
print(miVariable3)

#miVariable3 = miVariable3 * 3
miVariable3 *= 3
print(miVariable3)

#miVariable3 = miVariable3 / 2
miVariable3 /= 2
print(miVariable3)

#Operaciones sobre cadenas de texto
# + Concatenacion 'Ho' + 'la'  = 'Hola'
# * Repeticion 'Helo word' * 3 = 'Hello word, hello word, hello word'



# Operadores de comparacion
b = 4
d = 4
# Operador igual
resultado = b == d  # Comparamos si son iguales
print(resultado)


# Operador Diferente
resultado = b != d
print(resultado)

# Operador Mayor que
resultado = b > d
print(resultado)

# Operador Menor que
resultado = b < d
print(resultado)

# Operador menor o igual que
resultado = b <= d
print(resultado)

# Operador Mayor o igual que
resultado = b >= d
print(resultado)
'''
'''
# Ejercicio: Numero par o impar
num = int(input('Ingrese un numero: '))
print(f'El residuo de la division es: {num % 2}')
if (num % 2) == 0:
    print(f'El valor del numero es: {num}. Es un numero par')
else:
    print(f'El valor del numero es: {num}. Es un numero impar')
'''
'''
# Ejercicio: Determinar si es mayor de edad
edadAdulto = 18
edadPersona = int(input('Digite su edad: '))
if edadPersona >= edadAdulto:
    print(f'Su edad ed: {edadPersona}. Es mayor de edad')
else:
    print(f'Su edad es: {edadPersona}. Es menor de edad')
'''


'''
CLASE 5: OPERADORES LOGICOS 

a = False
b = True

#AND ambos tienen q ser true para que de true (binario)
resultado = a and b
print(resultado)

# OR con que uno sea true el resultado es true (binario)
resultado = a or b
print(resultado)

# NOT invierte el valor, si es true da false y viseversa (unario)
resultado = not a
print(resultado)
'''
'''
# Ejercicio: Valor dentro de un rango

num = int(input('Digite un valor numerico: '))
valorMinimo = 0
valorMaximo = 5
dentroRango = num >= valorMinimo and num <= valorMaximo
if dentroRango:
   print(f'El valor {num} esta dentro del rango')
else:
    print(f'El valor {num} NO esta dentro del rango')
'''
'''
# Ejercicio con el operador OR / operador NOT
vacaciones = False
diaDescanso = False
puedeAsistir = vacaciones or diaDescanso
if not (puedeAsistir):
    print(f'No podrá asistir porque tiene que trabajar')
else:
    print(f'Puede asistir al juego')
'''


'''
# Ejercicio: Verificar si esta en sus 20's o 30's años (rango 20 30(? segun el profesor)
edad = int(input('Digite su edad: '))

#if (edad >= 20 and edad<= 30) or (edad >= 30 and edad <= 40):
if (20 <= edad <30) or (30 <= edad < 40):  # Sintaxis simplificada del AND
    print("Estas dentro del rango de los 20's 30's")
else:
    print('No estas dentro del rango')

#veinte = edad >= 20 and edad<= 30
#print(veinte)
#treinta = edad >= 30 and edad <= 40
#print(treinta)

if veinte:
    print("Estas dentro de los 20's años")
elif treinta:
    print("Estas dentro de los 30's años")
else:
    print('No estas dentro del rango de edad')

# Otra forma de usar el if
if veinte or treinta:
    if veinte:
        print("Estas dentro de los 20's años")
    elif treinta:
        print("Estas dentro de los 30's años")
else:
    print('No estas dentro del rango de edad')
'''

'''
# Ejercicio: El mayor de dos numeros

num1 = int(input('Digite un numero: '))
num2 = int(input('Digite otro numero: '))

if (num1 > num2):
    print(f'El numero mayor es: {num1}')
elif (num2 > num1):
    print(f'El numero mayor es: {num2}')
else:
    print('Los numeros ingresados son iguales.')
'''
'''
# Ejercicio: Tienda de libros
print('Ingrese los siguientes datos del libro.')
nombreLibro = input('Digite el nombre del libro: ')
idLibro = input('Digite ID del libro: ')
precio = float(input('Digite el precio del libro: '))
envioGratis = input('Indique si el envio es gratuito (True/False: ')

if envioGratis == 'True':
    envioGratis = True
elif envioGratis == 'False':
    envioGratis = False
else:
    envioGratis = 'El valor es incorrecto debe escribir True o False'

print(f
        Nombre: {nombreLibro}
        Id: {idLibro}
        Precio: ${precio}
        Envío gratuito?: {envioGratis}
)
'''

