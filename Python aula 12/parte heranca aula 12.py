class Veiculo:
    def __init__(self, marca:str, modelo:str, cor:str, ano:int) -> None:
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str, ano: int, qtde_portas: int) -> None:
        super().__init__(marca, modelo, cor, ano)
        self.qtde_portas = qtde_portas

class Moto(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str, ano: int, cilindradas:int) -> None:
        super().__init__(marca, modelo, cor, ano)
        self.cilindradas = cilindradas

class Bicicleta(Veiculo):
    def __init__(self, marca: str, modelo: str, cor: str, ano: int, marchas:bool)-> None:
        super().__init__(marca, modelo, cor, ano)
        self.marchas = marchas

carro1 = Carro(marca="Fiat", modelo="Palio", cor="Azul", ano=2004, qtde_portas=2)
moto1 = Moto(marca="Honda", modelo="500x", cor="branco", ano=2022, cilindradas= 500)
bicicleta1 = Bicicleta(marca="Caloi", modelo="bmx", cor="Verde", ano=2023, marchas=True)


print(carro1.ligar())
print(carro1.ligar_o_ar())
print(moto1.ligar())
print(bicicleta1.ligar())
