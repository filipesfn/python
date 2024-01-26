from tkinter import *

janelinha = Tk()

janelinha.title("Aula 1 Tkinter")

janelinha.geometry("400x400")

def saudar():
    nome = usuario_input.get()
    idade = int(idade_input.get())
    idade_futura = idade + 5
    print(f"Bem vindo, {nome}, sua idade daqui a 5 anos será: {idade_futura}!")
usuario_label= Label(text="Digite seu nome de usuário")
usuario_label.pack()

usuario_input = Entry()
usuario_input.pack()

idade_label = Label(text="Digite sua idade")
idade_label.pack()

idade_input = Entry()
idade_input.pack()



botao = Button(janelinha, text="Enviar", command=saudar)
botao.pack()

janelinha.mainloop()
