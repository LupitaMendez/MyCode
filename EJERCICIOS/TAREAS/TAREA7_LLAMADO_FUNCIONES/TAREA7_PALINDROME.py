"""La palabra es palíndrome, a través de función"""

def palindrome ():

    frase = input("Ingresa una frase: ")
    rever = frase [::-1]

    if frase ==rever:
        print("La palabra ingresada si es palindromo")
    else:
        print("La palabra ingresada no es palindromo")
    
    return frase

print(palindrome ())