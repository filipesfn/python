from tkinter import *

lista_de_cadastro = ["joao@email.com",
"maria@email.com",
"jose@email.com",
"ana@email.com",
"pedro@email.com",
"abel@email.com",
"patricia@email.com",
"amanda@email.com"]

janela = Tk()

janela.title("Nova conta")

label= Label(janela, text="Novo Usuário", font=("Arial", 12))
label.pack()


texto = Entry(janela, bg="lightgrey", fg="black")
texto.pack()

labelfantasma= Label(janela, text="", font=("Arial", 12))
labelfantasma.pack()

label1= Label(janela, text="Digite sua senha", font=("Arial", 12))
label1.pack()

labelfantasma1= Label(janela, text="", font=("Arial", 12))
labelfantasma1.pack()


texto1 = Entry(janela, bg="lightgrey", fg="black")
texto1.pack()

label2= Label(janela, text="Repita sua senha", font=("Arial", 12))
label2.pack()

labelfantasma2= Label(janela, text="", font=("Arial", 12))
labelfantasma2.pack()

texto2 = Entry(janela, bg="lightgrey", fg="black")
texto2.pack()

def buttonclick():
    # label1.config(text="Senha cadastrada com sucesso")

    email = texto.get()
    
    # if email not in lista_de_cadastro:
    #     labelfantasma.config(text="Novo email OK")
    #     if texto1.get() == texto2.get():
    #         print("Nova senha cadastrada com sucesso") 
    #     else:
    #         print("Senhas digitadas não são iguais")

    # else:
    #     labelfantasma.config(text='Email já cadastrado')
    
    quantidade_de_caracteres = texto1.get()

    if len(quantidade_de_caracteres) >= 8:
        print("Senha cadastrada com sucesso")
    else:
        print("A senha deve ter no mínimo 8 caracteres")

    senha = texto1.get()

    listaMaiusculo = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    listaminusculo = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    listanumeros = ["1","2","3","4","5","6","7","8","9","0"]
    listacaracteresespeciais = ["!#$%&'()*+,-./0123456789:;<=>?@", '*']
    
    # for i in senha
    temMaiuscula = False
    for i in listaMaiusculo:
        if i in senha:
            temMaiuscula = True

    temMinuscula = False
    for i in listaminusculo:
        if i in senha:
            temMinuscula = True
        else:
            labelfantasma2.configure(text="A senha deve ter pelo menos um caracter minúsculo")
            break

    temNumero = False
    for i in listanumeros:
        if i in senha:
            temNumero = True
        else:
            labelfantasma2.configure(text="A senha deve ter no mínimo um numero")
            break
    temEspecial = False
    for i in listacaracteresespeciais:
        if i in senha:
            temEspecial = True
        else:
            labelfantasma2.configure(text="A senha deve ter pelo menos um caracter especial")
            break

        
        
    if email not in lista_de_cadastro:
        labelfantasma.config(text="Novo email OK")
        if texto1.get() == texto2.get():
            print("Nova senha cadastrada com sucesso") 
        else:
            print("Senhas digitadas não são iguais")

    else:
        labelfantasma.config(text='Email já cadastrado')
   

    
    
    
    # if any(texto1.lower() for in senha):
    #     print("A senha pode ser utilizada")
    # else:
    #     print("A senha ter no minimo um caracter minusculo")


    
       



button = Button(janela, text="Cadastar", font=("Arial", 10, "bold"), command=buttonclick)
button.pack()





# novo_usuario = 

janela.mainloop()