
"""Calcular el área de un cuadrado a través de una función"""

def area_cuadrado ():
    lado = 0
    lado= input("Ingresa el valor del lado: ")
    lado = int(lado)
    area = lado*lado

    return area

print(area_cuadrado ())
