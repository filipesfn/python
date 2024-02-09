class Pessoa:
    def __init__(self, nome:str, idade:int, peso: float, genero:str) -> None:
        self.nome_da_pessoa = nome
        self.idade_da_pessoa = idade
        self.sobrenome_da_pessoa = "Silva"
        self.peso_da_pessoa = peso
        self.genero_da_pessoa = genero

pessoa1 = Pessoa(nome="Abel", idade= 28, peso= 75.6, genero= "Masculino")
pessoa2 = Pessoa(nome="Sid", idade=23, peso= 80, genero="Masculino")
pessoa3 = Pessoa(nome="Ludmilla", idade=19, peso=60, genero="feminino")
pessoa4 = Pessoa(nome="Hilda", idade=25, peso= 71, genero="Feminino")
                 
print (f"O cidadão {pessoa1.nome_da_pessoa}, de idade {pessoa1.idade_da_pessoa} anos, pesando {pessoa1.peso_da_pessoa} kgs, do genero {pessoa1.genero_da_pessoa} não tem antecedentes criminais!")

