from tkinter import *

janela = Tk()

janela.title("Média Final do Aluno")

janela.geometry("500x500")
janela.configure(background="#DBF4A7")

def media_global():
    exercicio_media1 = float(primeira_nota_input.get())
    if exercicio_media1 < 0 or exercicio_media1 > 10:
        erro1_label.configure(text="Digite uma nota válida", fg="red")
    exercicio_media2 = float(segunda_nota_input.get())
    if exercicio_media2 < 0 or exercicio_media2 > 10:
        erro2_label.configure(text="Digite uma nota válida", fg="red")
    exercicio_media3 = float(terceira_nota_input.get())
    if exercicio_media3 < 0 or exercicio_media3 > 10:
        erro3_label.configure(text="Digite uma nota válida", fg="red")
    media = (exercicio_media1 + exercicio_media2 + exercicio_media3) /3
    if media >= 7:
        resultado.configure(text=(f"Sua média final é: {media}, Resultado>: Aprovado"), bg="lightgreen")
    elif media <7:
        resultado.configure(text=(f"Sua média final é: {media}, Resultado>: Reprovado"), bg="lightred")
    elif media == 10:
        resultado.configure(text=(f"Sua média final é: {media}, Resultado>: Aprovado com distinção"), bg="darkblue")
    # elif media >10 or media <0:
    #     resultado.configure(text=(f"Sua média final é: {media}, Resultado>: Nota inválida"), bg="lightgrey")
    else:
        resultado.configure(text=("Média inválida, digite apenas notas válidas!"))

primeira_nota_label = Label(text="Digite a primeira nota do aluno:")
primeira_nota_label.pack()

primeira_nota_input = Entry()
primeira_nota_input.pack()

segunda_nota_label = Label(text="Digite a segunda nota do aluno:")
segunda_nota_label.pack()

erro1_label = Label(text="")
erro1_label.pack()

segunda_nota_input = Entry()
segunda_nota_input.pack()

erro2_label = Label(text="")
erro2_label.pack()

terceira_nota_label = Label(text="Digite a terceira nota do aluno:")
terceira_nota_label.pack()

terceira_nota_input = Entry()
terceira_nota_input.pack()

erro3_label = Label(text="")
erro3_label.pack()

botao = Button(janela, text="Calcular média do aluno", command=media_global)
botao.pack(pady=10)

resultado = Label(text="", background="#3C493F", foreground="#f0f7F4")
resultado.pack()


janela.mainloop()