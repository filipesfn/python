def media(n1,n2,n3):
    return (n1+n2+n3) / 3

nota1 = int(input("Digite a primeira nota: "))
nota2 = int(input("Digite a segunda nota: "))
nota3 = int(input("Digite a terceira nota: "))



resultado_media = media(n1=nota1,n2=nota2,n3=nota3)
print(resultado_media)

if resultado_media >= 7:
    print(f"Aprovado com a média {resultado_media:.2f}")
else:
    print("Reprovado")




