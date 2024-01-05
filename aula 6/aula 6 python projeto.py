lista_de_tarefas = []

def adicionar_nova_tarefa():
    dicionario_tarefa =  {
        "Descrição" : str(input("Digite a descrição da tarefa: ")),
        "Categoria": int(input("""
        Digite a categoria da tarefa: 
        1 - Doméstica
        2 - Trabalho
        3 - Estudos
        4 - Pessoal
        5 - Lazer
        """)),
        "Prioridade": int(input("""
        Digite a prioridade da tarefa:
        1 - Baixa
        2 - Média
        3 - Alta 
         """)),    
        "Concluído": False                                    
    }
    if dicionario_tarefa["Prioridade"] == 1:
        print("Tarefa adiável")
    elif dicionario_tarefa["Prioridade"] == 2:
        print("Tarefa deve ser realizada sem falta")
    elif dicionario_tarefa["Prioridade"] == 3:
        print("Tarefa necessita ser concluída com urgência")
    else:
        ...

    if dicionario_tarefa["Categoria"] == 1:
        print("Tarefa relacionada a obrigações do lar")
    elif dicionario_tarefa["Categoria"] == 2:
        print("Tarefa relacionada a obrigações do trabalho")
    elif dicionario_tarefa["Categoria"] == 3:
        print("Tarefa relacionada a obrigação com os estudos")
    elif dicionario_tarefa["Categoria"] == 4:
        print("Tarefa relacionada a obrigações com minha vida pessoal")
    elif dicionario_tarefa["Categoria"] == 5:
        print("Tarefa relacionada a lazer")
    else:
        ...


    lista_de_tarefas.append(dicionario_tarefa)
    return "Tarefa adicionada com sucesso"

def mostrar_tarefas():
    for i, item in enumerate(lista_de_tarefas):
        print(f"""
        {i+1}º
        Descrição: {item['Descrição']}
        Categoria: {item['Categoria']}
        Prioridade: {item['Prioridade']}
        Concluído: {item['Concluído']}
""")
        
def tarefa_concluida():
    for i, item in enumerate(lista_de_tarefas):
        print(f"""
        {i+1}º
        Descrição: {item['Descrição']}
        Categoria: {item['Categoria']}
        Prioridade: {item['Prioridade']}
        Concluído: {item['Concluído']}
""")
        tarefa_concluida = int(input("Digite o número da tarefa concluída: "))
        tarefa_selecionada = lista_de_tarefas[tarefa_concluida -1]
        tarefa_selecionada["Concluído"] = True

while True:
    menu = int(input("""
    Escolha uma das opções abaixo:
    1 - Adicionar nova tarefa
    2 - Visualizar tarefas pendentes de conclusão
    3 - Marcar tarefa como concluída
    4 - Visualizar tarefas por prioridade
    5 - Visualizar tarefas por categoria
    0 - Sair 
    """))

    match menu:
        case 1:
           adicionar_nova_tarefa()
        case 2:
            mostrar_tarefas()
        case 3:
            tarefa_concluida()
        case 4:
            print("Chamar a função para visualizar as tarefas por prioridade")
        case 5:
            print("Chamar a função para visualizar as tarefas por categoria")
        case 0:
            break
        

