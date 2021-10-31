# """Diccionaries"""

# """Example one"""
# products = {
#     "fruits" : "mango",
#     "veggies" : "apio"
# }
# print ()

# """Example one, se puede convertir en lista"""
# products = {
#     "fruits" : ["mango","banana"],
#     "veggies" : ["apio", "papa"],
#     "nuts" : ["peanuts"]
# }
# print (products)

# """ 1. Crear un diccionario con claves duplicadas, no se pueden duplicar """

# dict_duplicado = {
#     "2": 2,
#     "2": 7
# }
# print(dict_duplicado)

# """ 2. Crea un diccionario variado """
# varied_dict = {
#     "integer": 1,
#     "string": "hola",
#     "boolean": True,
#     "float": 35.99,
#     "list": [1, 2.5, "tres", False], 
#     "tupple":("hello",),
#     "another_dict": {"month": "enero", "year": 2021},
#     "set":{"apple", "banana", "cherry"},
# }
# print(varied_dict)

# """ 3. Crear un diccionario vacío"""
# empty_dict =  {
#     "productos": "compu"
# }
# print(empty_dict)
# empty_dict.clear()
# print("3. diccionario vacío")
# print(f"campos: {empty_dict}")

# """ 4. Copiar un diccionario"""
# dict_1 = {
#     "2": "dos",
#     "3": "tres",
#     "4": "cuatro"
# }
# print("Diccionario copiado")
# dict_2 = dict_1.copy()
# print ("Copiado")
# print (dict_2)

# """5. Acceder a un diccionario, accediendo a un valor por la clave"""
# dict_1 = {
#     "2": "dos",
#     "3": "tres",
#     "4": "cuatro" 
# }
# print (dict_1 ["2"])  #ejemplo 1
# print (dict_1.get ("9", "nada aqui"))  #ejemplo 2 con un campo que no existe 

# """6. Mostrar valores"""
# print ("Imprimir sólo valores")

# dict_1 = {
#     "2": "dos",
#     "3": "tres",
#     "4": "cuatro"
# }
# dict_values = dict_1.values()
# print(dict_values)

# """6.1. Mostrar sólo la Key"""
# print ("Imprimir sólo Key")

# dict_1 = {
#     "2": "dos",
#     "3": "tres",
#     "4": "cuatro"
# }
# dict_keys = dict_1.keys()
# print(dict_keys)

# """7. Imprimir clave y valor"""
# print ("Imprimir clave y valor")

# dict_1 = {
#     "2": "dos",
#     "3": "tres",
#     "4": "cuatro"
# }
# for key, value in dict_1.items():
#     print(key, value)


# """8. Insertar claves y valores si no existen"""
# print ("Insertar claves y valores si no existen")

# dict_1 = {
#     "2": "dos",
#     "3": "tres",
#     "4": "cuatro"
# }
# dict_1.update ({"5": "cinco"})
# print(dict_1)

 # """9. Insertar clave y valor si no existe; si existe lo retorna, no lo edita"""
# print ("Insertar claves y valores )

# dict_1 = {
#     "2": "dos",
#     "3": "tres",
#     "4": "cuatro"
# }
# dict_1.setdefault("7", "siete")
# dict_1.setdefault("7", "SIETE")
# print(dict_1)

 # """12. Insertar clave y valor si no existe; si existe lo retorna, no lo edita"""
# print ("Insertar claves y valores )

# dict_1 = {
#     "2": "dos",
#     "3": "tres",
#     "4": "cuatro"
# }
# dict_1 = {**dict_1, **{"6":"seis"}}
# print(dict_1)

# """13. Editar clave"""
# print ("Editar clave")

# dict_1 = {
#     "2": "dos",
#     "3": "tres",
#     "4": "cuatro"
# }
# dict_1 ["2s"] = dict_1.pop("2")
# print(dict_1)


"""14. Retornar un diccionario agregando con claves y valores declarados"""
print ("Editar clave")

campo = ["key1", "key2"]
valor = ""
dict3 = dict.fromkeys(campo, valor)
print(dict3)
