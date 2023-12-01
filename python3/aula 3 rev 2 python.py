alunos = []

for i in range(1,6):
    aluno = str(input(f"Digite o nome do {i}º aluno: "))
    nota = float(input(f"Digite a nota do {i}º aluno: "))
    alunos.append([aluno,nota])

print(alunos)


maior_nota = 0
nome_do_aluno = ""
for novo in alunos:
    if novo_nome[1] > maior_nota:
        maior_nota = novo_nome[1]
        nome_do_aluno = novo[0]

print(f"""
    Nome do(a) melhor aluno(a): {nome_do_aluno}
    Nota do(a) {nome_do_aluno}: {maior_nota}
""")
