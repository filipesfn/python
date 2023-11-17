nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

média  = (nota1 + nota2 + nota3 + nota4) / 4

if média == 10:
    print("Você foi aprovado com distinção")
elif média < 10 and média >= 7:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")

