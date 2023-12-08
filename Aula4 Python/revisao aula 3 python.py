cidadao = {
    "nome": str(input("Digite o nome do cidadao: ")),
    "idade": int(input("Digite a idade da cidadao: ")),
    "altura": float(input("Digite a altura da cidadao: ")),
    "salario": float(input("Digite salario da cidadao: "))
   }

if cidadao["idade"] > 18:
    print(f"O {cidadao['nome']} pode tirar habilitação")

else:
    print(f"O {cidadao['nome']} não pode tirar a habilitação")

if cidadao["salario"] <= 1500:
    print(f"O {cidadao['nome']} tá liso")

elif cidadao["salario"] > 1500 and cidadao["salario"] <= 3000:
    print(f"O {cidadao['nome']} tá bem")

elif cidadao["salario"] > 3000 and cidadao["salario"] <= 5000:
    print(f"O {cidadao['nome']} tá estribado")

else:
    print("Virou programador!")
 


