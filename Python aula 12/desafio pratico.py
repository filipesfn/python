class Conta:
    def __init__(self, numero_da_conta:int, titular_conta:str) -> None:
        self.numero_da_conta = numero_da_conta
        self.titular_da_conta = titular_conta
        self.saldo = 0
    
    def deposito(self,valor_deposito):
        self.saldo = self.saldo + valor_deposito
        return f"O valor depositado foi de {self.saldo}"
    def saque(self,valor_saque):
        self.saque = self.saldo - valor_saque
        return f"O valor sacado da conta foi de {saque}"
    def saldo_atual(self):
        return f"O saldo desta consta é de R${self.saldo}"

class ContaCorrente(Conta):
    def __init__(self, numero_da_conta: int, titular_conta: str, taxa_manutencao: float, limite_especial:int) -> None:
        super().__init__(numero_da_conta, titular_conta)
        self.taxa_manutencao = taxa_manutencao
        self.limite_especial = limite_especial

    def saldo_atual(self):
        return f"O saldo desta consta é de R${self.saldo} + "




