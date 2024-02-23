class Veiculo:
    def __init__(self, marca:str, modelo:str, ano:int, preco:float) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        self.velocidade_atual = 0

    def acelerar(self,velocidade_recebida):
        self.velocidade_atual += velocidade_recebida
        return f"O veículo {self.modelo} acelerou e está a {self.velocidade_atual} por hora"
    
    def freiar(self):
        if self.velocidade_atual > 10:
            self.velocidade_atual -= 10
            return f"O veículo {self.modelo} freiou e está a {self.velocidade_atual} por hora"
        else:
            self.velocidade_atual = 0
            return f"O veículo {self.modelo} parou"
    
    def buzinar(self):
        return "Som indefinido"
    

class Carro(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, preco: float, qtde_portas:int) -> None:
        super().__init__(marca, modelo, ano, preco)
        self.qtde_portas = qtde_portas
        self.ar_condicionado = False

    def ligar_o_ar(self):
        if self.ar_condicionado:
            return "O ar já está ligado"
        else:
            self.ar_condicionado = True
            return f"O carro {self.marca} {self.modelo} ligou o ar"
    
    def buzinar(self):
        return "Bi bi"
    

class Navio(Veiculo):
    def __init__(self, marca: str, modelo: str, ano: int, preco: float) -> None:
        super().__init__(marca, modelo, ano, preco)
    
    def buzinar(self):
        return "Fomm fom"
    

carro1 = Carro(marca="Fiat", modelo="Palio", ano=2004, preco=8500, qtde_portas=2)

navio1 = Navio(marca="Sei la", modelo="Titanic", ano=1911, preco=500000000)

print(carro1.acelerar(8))
print(carro1.acelerar(10))
print(carro1.freiar())
print(carro1.freiar())
print(carro1.freiar())
print(carro1.buzinar())
print(carro1.ligar_o_ar())
print(carro1.ligar_o_ar())