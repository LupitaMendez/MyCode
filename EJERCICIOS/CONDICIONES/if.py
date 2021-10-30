#carros = ["audi", "bMw", "subaru", "toyota"]

"""Imprimir todos los carros con la inicial en Mayúscula, excepto BMW, que todas las letras son mayúsculas"""
#for carro in carros:
 #   if carro.lower() == "bmw":
  #      print(carro.upper())
   #     print("Es mi marca favorita")
   # else:    
    #    print(carro.title())


"""Imprimir todos los carros excepto audi"""
#for carro in carros:
 #   if carro != "audi":
  #      print(carro)


"""Comparaciones con números"""
#edad = 18
#print(edad==18)

#numero_favorito = input ("Ingresa mi número favorito")
#if int(numero_favorito) == 15:
 #   print("Correcto ese es mi número favorito")
#else:
 #   print("Fallaste, ese no es")

"""Operadores booleanos"""
#edad = 20
#print(edad<25)
#print(edad>25)
#print(edad<=25)
#print(edad>=25)

"""Múltiples condiciones"""

"""Operador and"""
#edad = 15
#if edad >= 12 and edad <= 18:
   # print("eres un adolescente")

"""Operador or o disyunción"""

# v v = v
# v f = v
# f v = v
# f f = f

#edad = 15

#if edad >= 12 and edad <= 18:
 #   print("eres un adolescente")
#if edad < 12 or edad > 18:
 #   print("no eres un adolescente")


"""Búsqueda dentro de uan lista"""
#numeros = [2, 3, 7, 9, 10, 11]
#busqueda = 2

#if busqueda in numeros:
 #   print ("Si se encontró")
#else:
 #   print ("no se encuentra")

"""Calcular el costo del ticket en selva mágica"""        
#edad = 17

#costo = 0
#if edad < 4:
 #   costo = 0
#elif edad < 18:
 #   costo = 80
#else:
 #   costo = 150

#print(f"Debes pagar $ {costo} pesos")

#edad = 30

#costo = 0
#if edad < 4:
 #   costo = 0
#else:
    #if edad < 18:
   #     costo = 80
  #  else:
 #       costo = 150

#print(f"Debes pagar $ {costo} pesos")

edad = 17

costo = 0

if edad < 4:
    costo = 0
if edad < 18:
    costo = 80
if edad >= 18:
    costo = 150

print(f"Debes pagar $ {costo} pesos")






