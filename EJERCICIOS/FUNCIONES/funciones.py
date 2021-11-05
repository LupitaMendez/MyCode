
"""sumar números"""
def sumar_numeros():
    resultado = 20 + 2

    return resultado


print(sumar_numeros())


"""Dividir números"""
def Dividir_numeros():
    resultado2 = 20 / 2

    return resultado2


print(Dividir_numeros())

"""nombre declarándola en sí misma"""
def dar_nombre(name):
    return name

print(dar_nombre("Panchito")) #se pone el argumento

"""restar números"""
def restar_numeros(a, b):
    resultado = a-b
    return resultado

print(f"Su resultado es: {restar_numeros(5,3)}")

"""multiplicar números"""
def multiplicar_numeros(a, b):
    resultado = a*b
    return resultado

print(f"Su resultado es: {multiplicar_numeros(5,3)}")


"""Dividir números"""
def dividir_numeros(a, b):
    resultado = a/b
    return resultado

print(f"Su resultado es: {dividir_numeros(5,3)}")

"""Funcion 1"""
def hello_world(name):
    return f"Hello {name.title()}"

