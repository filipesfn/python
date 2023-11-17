sexo = str(input("Digite seu sexo: ")).lower().strip()


if sexo == "m":
    print(f"Você é do sexo masculino")
elif sexo == "f":
    print(f"Você é do sexo feminino")
elif sexo == "x":
    print(f"Você é não binário")
else:
    print(f"Digite um sexo válido")
