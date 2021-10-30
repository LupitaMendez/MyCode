usuarios = ['admin','boss','vendedor','gerente']

for usuario in usuarios:
    if usuario == 'admin':
        print (f"Hola,{usuario}, ¿Quieres visualizar el reporte de uso?")
    else: 
        print (f"Hola {usuario}, ¡es usted bienvenido!")
