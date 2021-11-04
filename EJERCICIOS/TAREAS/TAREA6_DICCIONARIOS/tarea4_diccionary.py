"""Busca 5 palabras en el diccionario o enciclopledia y crea un programa que permita consultar la definición de esas palabras"""

Diccionario = {
    'arrebol': 'Efecto de la luz del sol al proyectarse sobre las nubes matutinas y de la arde, que se le otorga tonalidades rojizas',
    'Bonhomía' : 'Afabilidad, sencillez, bondad y honradez en el carácter',
    'Cagaprisas' : 'Persona que es impaciente, quien tiene prisa siempre',
    'Desleír' : 'Disolver algo, de contextura sólida o pastosa, en un líquido',
    'Ful' : 'Faso, fallido, que posee poco valor'
}

# print(Diccionario)

llave = input ("Ingresa la palabra de la que quieras saber su significado: ")

print(Diccionario[llave])