class Animal:
    def __init__(self, nome:str, raca:str, cor: str, peso=float) -> None:
        self.nome = nome
        self.raca = raca
        self.cor = cor
        self.peso = peso

    def comer(self, nome_comida):
        return f"O animal {self.nome} está comendo {nome_comida}."
    def dormir(self):
        return f"O animal {self.nome} está dormindo."
    
class Cachorro(Animal):
    def __init__(self, nome: str, raca: str, cor: str, peso=float, pedigree=bool) -> None:
        super().__init__(nome, raca, cor, peso)
        self.pedigree = pedigree
    def pegar_bolinha(self):
        return f"O animal {nome} foi pegar a bolinha."
class Papagaio(Animal):
    def __init__(self, nome: str, raca: str, cor: str, peso=float, asa_cortada=bool) -> None:
        super().__init__(nome, raca, cor, peso)
        self.asa_cortada = asa_cortada
    def voar(self):
        return f"O papagaio esta voando"
    
cachorro1 = Cachorro(nome="Bruno",raca="Bacê", cor="preto e laranja", peso=5.6)
papagaio1 = Papagaio(nome="Didi",raca="Papagaio Cinza", cor="Cinza", peso=2.1, asa_cortada=True)
porco1 = Animal(nome="Cacá", raca="rabicó", cor="rosa", peso=22.6)
                
print(cachorro1.comer("Osso"))
print(cachorro1.dormir())
print(cachorro1.pegar_bolinha())


print(papagaio.comer("Biscoito"))
print(papagaio.dormir())
print(papagaio.voar())

print(porquim.comer("Lavagem"))
print(porquim.dormir())
                




    
      
