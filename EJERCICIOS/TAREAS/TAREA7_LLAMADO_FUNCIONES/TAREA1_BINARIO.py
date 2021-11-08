
#Convertir valor númerico a número binario con format
def num_to_binario ():

    numero = input ("Ingrese el valor numérico del 1-1024 que desee convertir a número binario ")
    numero = int(numero)
    binario = bin(numero)

    print(binario)
    
    return binario
  
print(num_to_binario())
