def saudacao(hora):
    if hora > 0 <= 12:
        return"Bom dia!"
    elif hora > 12 <= 18:
        return"Boa tarde!"
    else:
        return"Boa noite!"


resultadosaudacao =  saudacao(int(input(f"Digite um hora: ")))

print(resultadosaudacao)
