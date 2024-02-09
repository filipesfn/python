class Cachorro:
    def __init__(self, nome:str, raca:str, idade:int) -> None:
        self.nome = nome
        self.raca = raca
        self.idade = idade


cachorro1 = Cachorro(nome="Rex", raca="Labrador", idade= 3)
cachorro2 = Cachorro(nome="Like", raca="Poodle", idade=5)

print(f"O nome do primeiro cachorro é {cachorro1.nome}")
print(f"O nome do segundo cachorro é {cachorro2.nome}")
