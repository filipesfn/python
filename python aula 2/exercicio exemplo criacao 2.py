lista_de_compras = ["banana", "mamão", "maçã", "abacaxi"]

while True:
    nova_fruta = str(input("Digite uma nova fruta a ser incluída: "))
    if nova_fruta == "sair":
        break

    lista_de_compras.append(nova_fruta)

