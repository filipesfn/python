cadastro_produtos = []

while True:
    cadastro_item = {
        'nome do item': str(input("Digite o nome do item: ")),
        'valor do item' : float(input("Digite o valor do item: "))                               

    }
    if cadastro_item['nome do item'] == "sair":
        break
    cadastro_produtos.append()