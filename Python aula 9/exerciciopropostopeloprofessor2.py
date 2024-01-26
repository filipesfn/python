from tkinter import *

janela = Tk()

janela.title("Exercício proposto pelo professor")

janela.geometry("500x500")


def ficha_criminal():
    idadedocara = int(idade1_input.get())
    nomedocara = str(nome1_input.get())
    if idadedocara <= 2006:
        print(f" {nomedocara} já pode ser preso!") 
    else:
        print(f"{nomedocara} ainda não pode ser preso!")
        
    
idade1_label = Label(text="Digite o ano do seu nascimento:")
idade1_label.pack()

idade1_input = Entry()
idade1_input.pack()

nome1_label = Label(text="Digite o seu nome:")
nome1_label.pack()

nome1_input = Entry()
nome1_input.pack()

botao = Button(janela, text="Enviar", command=ficha_criminal)
botao.pack()


janela.mainloop()