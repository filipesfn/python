def contar_vogais(palavra):
    contador_vogais = 0

    for letra in palavra:
        if letra.lower() in 'aeiouáâãéêíàóõôú':
            contador_vogais += 1
    return contador_vogais

palavra = str(input("Digite uma palavra: "))
print(f"A palavra digitada contém {contar_vogais(palavra)} vogais")
