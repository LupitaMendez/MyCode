"""5.1 Lista de lugares que me gustaría visitar a través de funciones"""
def lugares_to_visit ():

    import sys
    lista = ["Islandia", "Canadá", "Cuba", "Groenlandia", "Irlanda", "Japón"]
    print(f"{lista[0]}, {lista[1]}, {lista[2]}, {lista[3]}, {lista[4]}, {lista[5]}") #opción 1
    print(lista) #opción 2

    #sorted(list,*,key=None,reverse=False)
    print(sorted(lista)) #Opción 1
    print(lista)

    print(sorted(lista, reverse=True)) #Opción 1
    print(lista)

    lista.reverse()
    print(f"La lista en reversa quedará guardada así: {lista}" )

    lista.reverse()
    print(f"La lista inicial es: {lista}" )

    lista.sort()
    print(f"La lista ordenada es: {lista}" )

    lista.sort(reverse=True)
    print(f"La lista ordenada en orden inverso es: {lista}" )

    return 

print(lugares_to_visit())