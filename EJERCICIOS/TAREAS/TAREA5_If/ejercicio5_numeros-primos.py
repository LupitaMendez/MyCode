# """Generador de números primos menores al 1000"""
# list = []

# for value in range (1,4):
#     listas = (value*2)+1
#     list.append(listas) 
# for value in range (5,7):
#     listas = (value*2)+1
#     list.append(listas)
# for value in range (9,11):
#     listas = (value*2)+1
# # for value in range (11,12):
# #     listas = (value*2)+1
# list.append(listas)
# print(list)


"LO BUSQUÉ, PORQUÉ NO ENCONTRÉ LA FÓRMULA MATEMÁTICA PARA DETERMINARLO"
n = int(input('Give me a number: ')) 
h = n*n+2
 
lista = []
for x in range(2, h):
	    condicion = True
 
	    for divisor in range(2, x):
		    if x % divisor == 0:
			    condicion = False
			    break
 
	    if condicion and len(lista)<n:
		    lista.append(x)
 
print(lista)