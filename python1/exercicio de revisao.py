ano = int(input("Digite sua data de nascimento"))

idade = 2023 - ano

if idade >=0:
    if idade >= 18:
        print(f"Você já pode ser preso")
    else:
        print(f"Você ainda está livre da prisão")
else:
    print("Digite uma ano válido")
    
      
