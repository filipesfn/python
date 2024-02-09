# Importing Tkinter library
from tkinter import *
from tkinter import ttk

# Defining colors
co1 = "#feffff"  # white/branca
co2 = "#38576b"  
co3 ="#ECEFF1"
co4='#FFAB40' # Orange/laranja
fundo = "#3b3b3b" # black/preta

# Creating the main window
janela = Tk()
janela.title('')
janela.geometry('235x318')
janela.configure(bg=co1)

# Creating a function to enter numbers and mathematical operations
def entrar_valor(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    valor_texto.set(todos_valores)

# Creating a function to calculate the result
def calcular():
    global todos_valores
    resultado = str(eval(todos_valores))
    valor_texto.set(resultado)
    todos_valores = ""

# Defining variables
todos_valores = "" 
valor_texto = StringVar()

# Creating the calculator screen
app_tela = Label(janela,textvariable=valor_texto,width=16,height=2, padx=7, relief="flat", anchor="e",bd=0, justify=RIGHT, font=('Ivy 18 '), bg='#37474F', fg=co1)
app_tela.grid(row=1, column=0, sticky=NW)

# Creating the calculator buttons
b_1 = Button(janela,command = lambda: entrar_valor('1'), text="1", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_1.grid(row=2, column=0, sticky=NW)
b_2 = Button(janela,command = lambda: entrar_valor('2'), text="2", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_2.grid(row=2, column=1, sticky=NW)
b_3 = Button(janela,command = lambda: entrar_valor('3'), text="3", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_3.grid(row=2, column=2, sticky=NW)
b_4 = Button(janela,command = lambda: entrar_valor('4'), text="4", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_4.grid(row=3, column=0, sticky=NW)
b_5 = Button(janela,command = lambda: entrar_valor('5'), text="5", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_5.grid(row=3, column=1, sticky=NW)
b_6 = Button(janela,command = lambda: entrar_valor('6'), text="6", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_6.grid(row=3, column=2, sticky=NW)
b_7 = Button(janela,command = lambda: entrar_valor('7'), text="6", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_7.grid(row=3, column=3, sticky=NW)
b_8 = Button(janela,command = lambda: entrar_valor('8'), text="6", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_8.grid(row=3, column=4, sticky=NW)
b_9 = Button(janela,command = lambda: entrar_valor('9'), text="6", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_9.grid(row=3, column=5, sticky=NW)
b_0 = Button(janela,command = lambda: entrar_valor('0'), text="6", width=5, height=2, bg=co3, fg=fundo,font=('Ivy 13 bold'),relief=RAISED, overrelief=RIDGE)
b_0.grid(row=3, column=6, sticky=NW)