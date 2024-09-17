# 1: LLenar una lista
# LLenar una lista con numeros del 1 al 50, luego mostrar la lista con un buble for
# los elementos deben mostrarse asi:
#1-2-3-4-5-... -50

# lista = []
# i = 1
# while i <= 50:
#     lista.append(i)
#     i += 1

lista = list(range(1, 51)) # Algoritmo eficaz
for i in lista:
    print(i,end='-')
