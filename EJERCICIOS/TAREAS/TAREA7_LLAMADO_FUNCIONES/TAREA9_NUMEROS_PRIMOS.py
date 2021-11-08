
def numeros_primos():
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

	return lista

print (numeros_primos())