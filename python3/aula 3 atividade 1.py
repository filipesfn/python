lista_aluno = []

for i in range (1,6):
    cadastro_aluno = {
    'nome': str(input("Digite o nome do aluno: ")),
    'CPF': int(input("Digite o numero do seu CPF: ")),
    'Endereço': str(input("Digite seu endereço: ")),
    'RG': int(input("Digite o numero do seu RG: ")),
    'Série': int(input("Digite a série do aluno: "))
}
    
    lista_de_usuarios.append(cadastro_aluno)

print(cadastro_aluno)