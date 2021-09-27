#Conversor de números a ascii

caracter = input ("Ingresa un número de la A-Z: ")
for letra in caracter:
    print("El valor de {} es {}".format(letra, ord(letra)))