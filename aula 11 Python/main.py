class Moto:
    def __init__(self, marca:str, modelo:str, ano:int, cor:str, cilindrada:float, placa:str, multas:list) -> None:
        self.marca_da_moto = marca
        self.modelo_da_moto = modelo
        self.ano_da_moto = ano
        self.cor_da_moto = cor
        self.cilindrada_da_moto = cilindrada
        self.placa_da_moto = placa
        self.multas_da_moto = multas

    def buzinar(self):
        return f"A moto {self.modelo} está buzinando, sai da frente"
    
    def acelerar(self):
        self.velocidade_atual +=20
        return f"A moto está acelerando"
    
    def freiar(self):
        self.velocidade_atual -=10
        return f"A moto está freiando"

moto1 = Moto(marca=:"Honda", Modelo="Bros", ano=2020, cor="Azul", cilindrada=149,7, placa=P4FLN48, multas=["Infração":"Andando de chinelo", "Valor":"300", "Gravidade": "Leve"])

moto2 = Moto(marca="Yamaha", modelo="Factor", ano=2022, cilindrada=162.7, placa=Y8GYT69, multas="Infração":"Conduzindo sem capacete", "Valor":"800", "Gravidade":"Alta")

moto3 = Moto(marca="Tesla", modelo="Future", ano=2024, cilindrada=200, placa=F1LIP32, multas="Infração":"Trafegando pela via de ciclistas", "Valor":"600", "Gravidade":"Alta")

moto4 = Moto(marca"Honda", modelo="CB500", ano=2023, cilindrada=180.6, placa=H3DOA11, multas="Infração":"Passar no sinal vermelho", "Valor":"500", "Gravidade":"Média")

print(moto1.buzinar()
      moto1.acelerar((velocidade = 40))
      moto1.acelerar()
