class Fatura:
    def __init__(self, nome="str", preco=float, quantidade=int, valor=float) -> None:
        self.nome_do_item = nome
        self.preco_do_item = preco
        self.quantidade_do_item = quantidade 
        self.valor_total = 0

    def gerar_fatura(self):
        self.valor_total = self.preco_do_item * self.quantidade_do_item
        return f"O valor total da fatura ficou R$ {self.valor_total:.2f}"
    
fatura1 = Fatura(nome="Mouse", preco=25.90, quantidade=12)
fatura2 = Fatura(nome="Teclado", preco=49.90, quantidade=27)

print(fatura1.gerar_fatura())
print(fatura2.gerar_fatura())


