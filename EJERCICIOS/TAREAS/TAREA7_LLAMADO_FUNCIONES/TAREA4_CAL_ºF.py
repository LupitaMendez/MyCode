"""Pide un valor en grados centigrados y lo muestra en grados farenheit, a través de una función"""

def grados_centigrados ():

    grados_cel = input ("Ingresa el valor en grados Celsius: ")
    grados_cel= float(grados_cel)
    farenheit = ((grados_cel * 1.8 + 32))

    return farenheit
print (grados_centigrados())

