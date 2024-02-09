class Calculadora:
    def __init__(self, n1, n2) -> None:
        self.numero1 = n1
        self.numero2 = n2


    def somar(self, n1:float, n2:float)
    return n1 + n2

    def subtrair(self):
    return n1 + n2

    def multiplicar(self):
    return n1 * n2

    def dividir(self):
    if n2 != 0:
        return n1 / n2
    else:
        return "Não pode dividir por 0"
    
 calculadora1 = calculadora()

while True: 
    menu = int(input("""
    Escolha uma opção
    1 - Somar
    2 - Subtrair
    3 - Multiplicar
    4 - Dividir
    0 - Sair
"""))
    
    match menu:
        case 1:
            print(somar(n1, n2))
        case 2:
            print(subtrair(n1, n2))
        case 3:
            print(multiplicar(n1, n2))
        case 4:
            print(dividir(n1, n2))
        case 0:
            break
        case _:
            print("Opção inválida")

