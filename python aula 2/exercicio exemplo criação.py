lista_de_compras = ["banana", "mamão", "maçã", "abacaxi"]

for lista in range(4):
    novo_item = str(input("Digite um novo item a ser incluído: "))
    lista_de_compras.append(novo_item)

print(lista_de_compras)