"""MENSAJE PARA AMIGOS, CON LLAMADO A FUNCIÓN"""
def amigos ():

    lista = ["Brianda", "Sergio", "Alfredo", "Fernando", "Uriel"]

    print (f"Mi mejor amiga es:{lista[0]}")
    print (f"Mi mejor amigo es:{lista[1]}")
    print (f"Mi roomie es:{lista[2]}")
    print (f"Mi mejor amigo en la universidad fué:{lista[3]}")
    print (f"Mi mejor amigo en el trabajo fué:{lista[4]}")

    mensaje = "Lo mejor de trabajar en DEMIM has sido tú:"

    print (f"{mensaje} {lista [0]} ")
    print (f"{mensaje} {lista [1]} ")
    print (f"{mensaje} {lista [2]} ")
    print (f"{mensaje} {lista [3]} ")
    print (f"{mensaje} {lista [4]} ")

    return mensaje

print(amigos())