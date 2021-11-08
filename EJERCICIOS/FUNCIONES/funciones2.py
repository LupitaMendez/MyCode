"""Importar una función"""

from funciones import (hello_world, sumar_numeros, restar_numeros)

NAMES = ["lupita" , "marc", "joe"]

def my_funcion ():
    name = NAMES [0]
    print(hello_world(name))

my_funcion()

"""Tarea encapsular programas en su propia función"""
