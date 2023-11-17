i = 0
frase = str(input("Digite uma frase: "))

for letra in frase:
    if letra in 'aeiou':
        i = i+1

print(f"A quantidade de vogais é {i}")