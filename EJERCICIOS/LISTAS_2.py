"""Lista con agunos presidentes de México"""
#presidentes = ["Andres Manuel", "Enrique Pena", "Felipe Calderón", "Vicente Fox"]

# presidentes[0]
#for presidente in presidentes:  #For iterar listas 
  #  print(f"Hola {presidente}, ¿Cuánto dinero te robaste?")
  #  print("¡Devuelve el dinero, no seas ratero!")

"""Función Rango range()"""
  #Generador de números secuenciales
#for valor in range(1,1000):
 #   print(valor)


#presidentes = ["Andres Manuel", "Enrique Pena", "Felipe Calderón", "Vicente Fox"]
#print(presidentes [0])
#for indice in range (0,len(presidentes)):
 #  print(presidentes [indice])

#for valor in range(0, 20, 2):
 #   print(valor)
 
#print(list(range(0,5)))

#for valor in range(20):
   # print(valor)

"""Código para generar la lista de cuadrados de un rango versión 1"""
#cuadrados = []
#for value in range (1, 11):
 #   cuadrado = value ** 2
  #  cuadrados.append(cuadrado)
#print(cuadrados)


#digits = list(range(10))
#print (digits)
#print(max(digits))
#print(min(digits))
#print(sum(digits))
#print(sum(digits)/len(digits))

"""Código para generar la lista de cuadrados de un rango versión 1"""
#cuadrados = []
#for value in range (1, 11):
 #   cuadrado = value ** 2
  #  cuadrados.append(cuadrado)
#print(cuadrados)

"""Código para generar lalista de cuadrados de un rango versión 2"""
#cuadrados = [value ** 2 for value in range (1,11)]
#print(cuadrados)

#cuadrados = [str(value) for value in range (1,11)]
#print(cuadrados)

#Tupla cuando sólo tiene un valor
#t = (1,)

"""vaciar una lista"""
#invitados = ["luis", "jose", "adrian", "Pablo"]
#invitado = invitados.pop(0)
#print(f"{invitado} tú ya no estás invitado")
#invitado = invitados.pop()
#print(f"{invitado} tú ya no estás invitado") 

"""Esctructura iterativa"""
#invitados = ["luis", "jose", "adrian", "Pablo"]

#while len(invitados)> 2:
 #   invitado = invitados.pop() 
  #  print(f"{invitado} Tú ya no estás invitado")
#print(invitados)

presidentes = ["Andres Manuel", "Enrique Pena", "Felipe Calderón", "Vicente Fox"]
#ultimos_presidentes = presidentes[0:2] 
#ultimos_presidentes = presidentes[:2] 
#ultimos_presidentes = presidentes[3:] 
#ultimos_presidentes = presidentes[-1:] 
#ultimos_presidentes = presidentes[-2:] 
#print(ultimos_presidentes)

for presidente in presidentes [1:]:  #For iterar listas 
    print(f"Hola {presidente}, ¿Cuánto dinero te robaste?")
    print("Devuelve el dinero, no seas ratero")
