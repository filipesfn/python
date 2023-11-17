letra = str(input("Digite uma letra: ")).lower()

if len(letra) == 1:
    if letra in 'aeiou':
        print(f"Essa letra é uma vogal")
    elif letra in 'bcdfghjklmnpqrstvwxyz':
        print(f"Essa letra é uma consoante")
    else:
        print(f"Digite uma letra válida")


