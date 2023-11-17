contador_vogais = 0
contador_consoantes = 0
frase = str(input("Digite uma frase: "))

for letra in frase:
    if letra in 'aeiou':
        contador_vogais = contador_vogais +1
    elif letra in 'bcdfghjklmnpqrstvxyz':
        contador_consoantes = contador_consoantes +1
print(f"A quantidade de vogais é {contador_vogais}")    
print(f"A quantidade de consoantes é {contador_consoantes}")