"""Juego de adivinar el numero secreto"""
"""método uniforme para generar un numero aleatorio entre 1 y 100"""

import random
aleatorio = random.randint(1, 100)
print(aleatorio)

numero = input(f"Intenta adivinar el número secreto, ingresa un número entre el 1 y el 100: ")

while int(numero) != aleatorio:
    print("No adivinaste el número secreto, inténtalo de nuevo")
    numero = input(f"Intenta adivinar el número secreto, ingresa un número entre el 1 y el 100: ")
else:
    print(f"Adivinaste el número secreto, ¡el numero secreto es: {numero}!") 


    
