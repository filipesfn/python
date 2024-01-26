from tkinter import *

janela = Tk()

janela.title("Aprendendo cores")

janela.geometry("500x500")
janela.configure(background="#7DDE92")

def mostrar_altura():
    altura = float(altura_input.get())
    resultado.configure(font=("Arial", 16, "bold", "italic"), text=(f"Sua altura é: {altura}m."))

altura_label = Label(text="Digite sua altura", foreground="red", background="blue")
altura_label.pack()

altura_input = Entry()
altura_input.pack()


botao = Button(janela, text="Enviar",bg="#FF478E", fg="lightblue", width="16", height=2, command=mostrar_altura)
botao.pack()

resultado = Label(text="")
resultado.pack()


janela.mainloop()