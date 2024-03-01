id_livro =1
num_de_membro =1

class Livro:
    def __init__(self, titulo:str, autor:str, id:int):
        self.titulo = titulo
        self.autor = autor
        self.id = id
        self.disponivel = True

class Membro:
    def __init__(self, nome:str, numero_de_membro:int):
        self.nome = nome
        self.numero_de_membro = numero_de_membro
        self.historico_emprestimo = []

 
class Biblioteca:
    def __init__(self) -> None:
        self.catalogo_livros = []
        self.registro_membros = []
    
    def adicionar_livro(self):
        global id_livro
        titulo_livro = str(input("Digite o titulo do livro a ser adicionado: "))
        autor_livro = str(input("Digite o nome do autor do livro a ser adicionado: "))
        livro = Livro(titulo=titulo_livro, autor=autor_livro, id=id_livro)
        self.catalogo_livros.append(livro)
        id_livro +=1
        return "Livro adicionado com sucesso"

    def adicionar_membro(self):
        global num_de_membro
        cadastro_membro = str(input("Digite o nome do novo membro a ser incluído: "))
        membro = Membro(nome=cadastro_membro, numero_de_membro=num_de_membro)
        self.registro_membros.append(membro)
        num_de_membro +=1

    def emprestar_livro(self):
        livro_existe = False
        membro_existe = False
        emprestar = str(input("Digite o titulo do livro, seu autor ou id do livro a ser emprestado: "))
            
        if Livro.status == "disponivel":
            Livro.status = "emprestado"
            membro.borrowed_books.append(livro)
            print(f"Livro {livro.titulo} emprestado com sucesso!")
        else:
            print("Livro indisponível para empréstimo.")

    def devolver_livro(self):
        livro_existe = False

    def pesquisar_livro(self):
        livro_existe = False
        pesquisar = str(input("Digite o titulo do livro, seu autor ou id do livro a ser pesquisado: "))
        for livro_atual in self.catalogo_livros:
            if livro_atual.titulo.lower() == pesquisar.lower() or livro_atual.autor.lower() == pesquisar.lower() or str(livro_atual.id) == pesquisar:
                        livro_existe = True
                        print(f"""
                        Informações do Livro:
                        ID do livro: {livro_atual.id}
                        Título do livro: {livro_atual.titulo}
                        Autor do livro: {livro_atual.autor}
                        Disponibilidade do livro: {livro_atual.disponivel}

                
                        """)     
        if livro_existe == False:
            print("Livro não encontrado")

biblioteca1 = Biblioteca()

while True:
    menu = int(input("""
    Escolha uma opção
    1 - Adicionar Livro
    2 - Adicionar Membro
    3 - Emprestar Livro
    4 - Devolver Livro
    5 - Pesquisar Livro
    0 - Sair
    """))
    match menu:
        case 1:
            biblioteca1.adicionar_livro()
        case 2:
            biblioteca1.adicionar_membro()
        case 3:
            biblioteca1.emprestar_livro()
        case 4:
            biblioteca1.devolver_livro()
        case 5:
            biblioteca1.pesquisar_livro()
        case 0:
            print("Valeu meu fi, volte mais nao")
            break
        case _:
            print("Opção inválida")
