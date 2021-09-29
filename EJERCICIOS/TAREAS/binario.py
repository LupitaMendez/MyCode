
#Convertir valor númerico a número binanario con bin
entrada = input ("Ingrese el valor numérico del 1-1024 que desee convertir a número binario ")
entrada = int(entrada)
numero = format(entrada, "b")

print(numero)


#Convertir valor númerico a número binario con format
numero = input ("Ingrese el valor numérico del 1-1024 que desee convertir a número binario ")
numero = int(numero)
binario = bin(numero)

print(binario)


#Convertir valor númerico a número binario con format 2
numero = input ("Ingrese el valor numérico del 1-1024 que desee convertir a número binario ")
numero = int(numero)
binario = "{0:b}".format(numero)
print(binario)