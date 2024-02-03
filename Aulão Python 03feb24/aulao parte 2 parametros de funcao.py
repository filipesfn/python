def autenticar(conta, senha):
    if conta == "123" and senha == '123':
        print('Autenticado')
    else:
        print('Falha na autenticação')
autenticar('123', '123')
autenticar('012', '0123')

c = int(input('Digite a conta'))
s = int(input('Digite a senha: '))
autenticar()









    