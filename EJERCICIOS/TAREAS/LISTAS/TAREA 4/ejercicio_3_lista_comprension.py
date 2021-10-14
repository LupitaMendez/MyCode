
"""Crear una lista del 1-100, sacar la raíz cuadrada de cada número y almacenarla en otra lista"""
list = []
for value in range(1,101):
    listas = value
    list.append(listas)
print(list)

raiz = [value **(.5) for value in range (1,101)]
print(raiz) 

