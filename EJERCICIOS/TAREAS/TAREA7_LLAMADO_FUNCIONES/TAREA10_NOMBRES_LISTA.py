
def nombres_lista ():
    nombres = ["Guadalupe", "Rodrigo", "Oscar", "Alejandra", "Georgina", "Mauricio", "Marco", "Agustín", "Carlos", "Vicente"]

    nombres_dic = {}

    for i in range(len(nombres)):
        letra_key = nombres[i][0]
        nombres_dic.setdefault(letra_key, [])
        nombres_dic[letra_key].append (nombres [i])
 
    # print(nombres_dic)
    return nombres_dic

print(nombres_lista())