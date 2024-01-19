# cliente1 = {"Nome": Antonio, "CPF": 25698796375, Valor_da_compra: 623,14}

# cliente2 = {"Nome": Fabio, "CPF": 59762136943, Valor_da_compra: 769,29}

# cliente3 = {"Nome": Vanessa, "CPF": 59761369896, Valor_da_compra: 598,30}
import random

cadastro_de_clientes = []

def novo_cadastro():
    cadastro = {} 
    nome = str(input("Digite o nome do novo cliente: "))
        
    if nome.isalpha():
        CPF = str(input("Digite o CPF do novo cliente: "))

        if len(CPF) >= 11 and len(CPF) <= 14:
            Valor_da_compra = float(input("Digite o valor da compra do novo cliente: "))
            cadastro = {
                'nome': nome,
                'cpf': CPF,
                'Valor_da_compra': Valor_da_compra
            }
            print("Cadastrado com sucesso")
        else:
            print("CPF inválido")

        cadastro_de_clientes.append(cadastro)
    else:
        print("Nome inválido. Digite apenas letras.")

    

    cadastro_de_clientes.append(cadastro)

      
while True:
    menu = int(input("""
    Escolha uma opção:
    1 - Cadastrar cliente
    2 - Sair
    """))

    if menu == 1:
        novo_cadastro()
    elif menu == 2:
        break
    else:
        print(f"Digite uma opção válida")


cliente_maior_valor = max(cadastro_de_clientes, key=lambda x: x["Valor_da_compra"])
sorteio = random.choice(cadastro_de_clientes)

print(f"Parabéns {clientes['nome']}, CPF: {clientes['cpf']}, você foi o sorteado por ter feito uma compra no valor de R${clientes['Valor_da_compra']}")

print(f"O cliente com o maior valor de compra é {clientes['nome']}")



