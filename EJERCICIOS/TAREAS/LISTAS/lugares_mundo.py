"""5.1 Lista de lugares que me gustaría visitar"""
import sys

lista = ["Islandia", "Canadá", "Cuba", "Groenlandia", "Irlanda", "Japón"]
print(f"{lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}, {lista[4]}, {lista[5]}") #opción 1
print(lista) #opción 2


"""5.1 Imprimirlos los lugares en orden"""
#sorted(list,*,key=None,reverse=False)
print(sorted(lista)) #Opción 1
print(lista)


"""5.2 Imprimirlos los lugares en orden inverso utilizando 'sorted'"""
print(sorted(lista, reverse=True)) #Opción 1
print(lista)


"""5.3 Invertir el orden de la lista y que se guarde utilizando 'sorted', por error utilicé sorted"""
#lista = print(f" La Lista ordenada de manera inversa es: {sorted(lista,reverse=True)}"), al momento de imprimirlo me dice none.
#lista= sorted(lista, reverse=True) lo hice con reverse y no me había dado cuenta
#print(f" La nueva lista es:{lista}")


"""5.3 Invertir el orden de la lista y que se guarde utilizando 'Reverse'"""
lista.reverse()
print(f"La lista en reversa quedará guardada así: {lista}" )


"""5.4 Invertir nuevamente el orden de la lista y que se guarde utilizando como estaba inicialmente utilizando 'Reverse'"""
lista.reverse()
print(f"La lista inicial es: {lista}" )


"""5.5 Utilizar el método 'sort', para ordenar la lista'"""
lista.sort()
print(f"La lista ordenada es: {lista}" )


"""5.6 Utilizar el método 'sort', para ordenar la lista en orde inverso"""

lista.sort(reverse=True)
print(f"La lista ordenada en orden inverso es: {lista}" )