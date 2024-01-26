from tkinter import *

janelinha = Tk()

janelinha.title("Exercício 1")

janelinha.geometry("480x480")

def tela_inicio():
    exercicio_soma1 = float(primeiro_numero_input.get())
    exercicio_soma2 = float(segundo_numero_input.get())
    somatorio = exercicio_soma1 + exercicio_soma2
    print(f"A soma dos número é {somatorio}")
    segundo_numero_input.delete(0, END)
    primeiro_numero_input.delete(0,END)


primeiro_numero_label = Label(text="Digite o primeiro numero:")
primeiro_numero_label.pack()

primeiro_numero_input = Entry()
primeiro_numero_input.pack()

segundo_numero_label = Label(text="Digite o segundo numero:")
segundo_numero_label.pack()

segundo_numero_input = Entry()
segundo_numero_input.pack()

botao = Button(janelinha, text="Enviar", command=tela_inicio)
botao.pack()


janelinha.mainloop()

