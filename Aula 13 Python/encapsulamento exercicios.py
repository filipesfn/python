class Tarefa:
    def __init__(self, descricao:str, categoria:str, prioridade:str) ->None:
        self.descricao = descricao
        self.categoria = categoria
        self.prioridade = prioridade
        

class Projeto:
    def __init__(self, nome, objetivo, lista_tarefas:list) ->None:
        self.nome = nome
        self.objetivo = objetivo
        self.lista_tarefas = tarefas_lista

tarefa1 = Tarefa(descricao="Estudar POO em Python", categoria="Academica", prioridade="Alta")
tarefa2 = Tarefa(descricao="Aula de exercicios aerobicos", categoria="Saúde", prioridade="Média")
tarefa3 = Tarefa(descricao="Lavar a louca", categoria="Domestico", prioridade="Alta")
tarefa4 = Tarefa(descricao="Conhecer uma linguagem nova", categoria="Academico", prioridade="Alta")
tarefa5 = Tarefa(descricao="Ir para o supermódulo na Infinity", categoria="Academico", prioridade="Alta")
tarefa6 = Tarefa(descricao="Caminhar na praia", categoria="Saúde", prioridade="Média")
tarefa7 = Tarefa(descricao="Tomar creatina", categoria="Saúde", prioridade="Média")

projeto1 = Projeto(nome="Fit", objetivo="Ficar gostosão", lista_tarefas=[tarefa2,tarefa6, tarefa7])
projeto2 = Projeto(nome="Programador", objetivo="Ficar estribado", lista_tarefas=[tarefa1,tarefa4,tarefa5])


for item_atual in projeto1.lista_tarefas:
    print(f"""
    Descrição: {item_atual.descricao}
    Categoria: {item_atual.categoria}
    Prioridade: {item_atual.prioridade}
""")