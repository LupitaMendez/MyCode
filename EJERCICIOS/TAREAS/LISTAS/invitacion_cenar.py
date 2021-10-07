import sys

"""4.1Lista de personas para invitar a cenar"""
lista = ["Albert Einstein", "Jesucristo", "William shakespeare", "Pitágoras", "Nikola Tesla"]

print (f"Me gustaría invitarte a cenar {lista[0]}, tengo muchas preguntas qué hacerte.")
print (f"Me gustaría invitarte a cenar {lista[1]}, tengo muchas preguntas qué hacerte.")
print (f"Me gustaría invitarte a cenar {lista[2]}, tengo muchas preguntas qué hacerte.")
print (f"Me gustaría invitarte a cenar {lista[3]}, tengo muchas preguntas qué hacerte.")
print (f"Me gustaría invitarte a cenar {lista[4]}, tengo muchas preguntas qué hacerte.")


"""4.2Uno de mis invitados no podrá asistir a la cena, debo invitar a alguien más :O """
lista[2]= "Jeff Bezos"
print(f"William Shakespeare no podrá asistir a la cena, ya que no pudo revivir a tiempo jaja, pero he decididoo invitar a {lista[2]} ")

print (f"Te invito a mi cena {lista[0]}, ¡no puedes faltar habrá un invitado especial!.")
print (f"Te invito a mi cena {lista[1]},¡no puedes faltar habrá un invitado especial!.")
print (f"Te invito a mi cena {lista[2]}, ¡no puedes faltar habrá un invitado especial!.")
print (f"Te invito a mi cena {lista[3]}, ¡no puedes faltar habrá un invitado especial!.")
print (f"Te invito a mi cena {lista[4]}, ¡no puedes faltar habrá un invitado especial!")


"""4.3 Mesa más grande, habrá tres invitado más, ¡yujuuuu!"""
print ("Queridos invitados, he encontrado una mesa más grande, por lo cuál tendremos el gusto de tener a tres invitados más")

lista.insert(0,"James Blunt")
lista.insert(3, "Rihanna")
lista.append("robbie Williams")

print (f"{lista[0]}, tengo el gusto de invitarte a la mejor cena del año, ¡habrá gente de otro mundo!.")
print (f"{lista[1]}, tengo el gusto de invitarte a la mejor cena del año, ¡habrá gente de otro mundo!.")
print (f"{lista[2]}, tengo el gusto de invitarte a la mejor cena del año, ¡habrá gente de otro mundo!.")
print (f"{lista[3]}, tengo el gusto de invitarte a la mejor cena del año, ¡habrá gente de otro mundo!.")
print (f"{lista[4]}, tengo el gusto de invitarte a la mejor cena del año, ¡habrá gente de otro mundo!.")
print (f"{lista[5]}, tengo el gusto de invitarte a la mejor cena del año, ¡habrá gente de otro mundo!.")
print (f"{lista[6]}, tengo el gusto de invitarte a la mejor cena del año, ¡habrá gente de otro mundo!.")
print (f"{lista[7]}, tengo el gusto de invitarte a la mejor cena del año, ¡habrá gente de otro mundo!.")

"""4.4 Se cancela lo anterior, sólo hay mesa para tres, y debo elejir a los 2 afortunados"""
print ("Queridos invitados, lamento informarles que de último momento me avisaron que sólo hay mesa para 3, y desafortunadamente, debo cancelarles a la mayoría")

lista.pop(0)
print ("James Blunt, lamento decirte ésto pero fuiste de los rivales más débiles y por lo tanto no estás invitado a la cena")

lista.pop(2)
print ("Rihanna, lamento decirte ésto pero fuiste de los rivales más débiles y por lo tanto no estás invitado a la cena")

lista.pop(2)
print ("jeff Bezos, lamento decirte ésto pero fuiste de los rivales más débiles y por lo tanto no estás invitado a la cena")

lista.pop(2)
print ("Pitágoras, lamento decirte ésto pero fuiste de los rivales más débiles y por lo tanto no estás invitado a la cena")

lista.remove("Nikola Tesla")
print ("Nikola Tesla, lamento decirte ésto pero fuiste de los rivales más débiles y por lo tanto no estás invitado a la cena")

lista.remove("robbie Williams")
print ("Robbie Williams, lamento decirte ésto pero fuiste de los rivales más débiles y por lo tanto no estás invitado a la cena")

print(f"{lista[0]}, tú fuiste uno de mis dos favoritos, fuiste el afortunado para acudir a mi grandiosa cena")
print(f"{lista[1]}, tú fuiste uno de mis dos favoritos, fuiste el afortunado para acudir a mi grandiosa cena")

print(f"{lista[0]} y {lista[1]}, ¿Qué tal les pareció la cena, lo repetimos cada año?")