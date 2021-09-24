#Calcular el área de un cuadrado

# A= L*L

#Lado es un int
lado = 0
lado= input("Ingresa el valor del lado: ")

#area = lado*lad
lado = int(lado)

#area = lado * lado
area = lado**2

print (f"El area de tu cuadrado con l= {lado} es: {area}")
print (f"El area de tu cuadrado con l=" + str(lado) + "es:" + str(area))
