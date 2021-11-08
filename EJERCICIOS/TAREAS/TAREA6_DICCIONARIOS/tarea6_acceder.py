acceder = {
    'Lupita' : '940922',
    'Brianda' : '941123',
    'Edgar' : '850707',
    'Bruno' : '131912',
    'Lourdes' : '600211'
}

print ("¡Bienvenido a McDonals!")
usuario = input("Ingrese su usuario: ")
contraseña = input ("Ingrese su contraseña: ")

contraseña2 = acceder.get(usuario, ) #Se accede a través de la clave

if contraseña2 == contraseña:
    print(f"¡Bienvenid@ '{usuario}'!")
else:
    print("Usuario y/o contraseña erronea")