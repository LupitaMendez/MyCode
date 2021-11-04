"""Crea un diccionarios que contenga los datos de una persona"""
nombre = {
    "nombre(s)" : "Guadalupe",
    "apellido paterno": "Mendez",
    "apellido materno": "Pelayo",
    "edad": "27",
}
for key, value in nombre.items():
    print (key, value)

nombre.update ({"nacionalidad": "Mexicana"})

for key, value in nombre.items():
    print (key, value)