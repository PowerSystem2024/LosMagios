#=================CLASE 8================================

# CICLO WHILE (Mientras o Durante)

# contador = 0
# while contador < 15:
#     print(f'Ejecutamos nuestro ciclo while {contador}')
#     contador += 1
# else:
#     print(f'Fin del ciclo while')

# Imprimir numeros del 0 al 5 con el ciclo while
# maximo = 5
# contador = 0
#
# while contador <= 5:
#     print(contador)
#     contador += 1

# Imprimir numeros del 5 al 1
# minimo = 1
# contador = 5
# while contador >= minimo:
#     print(contador)
#     contador -= 1


# CICLO FOR (PARA)
# cadena = 'Hello'
# for letra in cadena:
#     print(letra)
# else:
#     print('Fin del ciclo for')

# Palabra reservada BREAK
# for letra in 'Alemania':
#     if letra == 'a':
#         print(f'Letra encontrada: {letra}')
#         # Luego de encontrar la letra 'a' minuscula y de imprimirla.
#         # El BREAK lo que va a hacer es romper con toda la estructura y terminar con todo el programa
#         break
# else:
#     print('Fin ciclo for')


# Palabra reservada CONTINUE
for i in range(6):   # del 0 al 5 ya que son 6 elementos
    if i % 2 == 0:
        print(f'Valor: {i}')

# Hacemos lo mismo usando CONTINUE

for i in range(6):
    if i % 2 != 0:
        continue #significa que va a eludir o anular todos los numeros impares
    print(f'Valor: {i}') #imprime los numeros pares

