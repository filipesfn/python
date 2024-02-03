# def areaTriangulo(b ,h):
#     print(b * h /2)
# areaTriangulo(8,9)

# def calcularAreaTriangulo(base, altura):
#     area = base * altura / 2
#     print(f'A área do triângulo = {}')

# base = float(int(input('Digite a metragem da base do triângulo: ')))
# altura = float(int(input('Digite a metragem da altura do triâgulo: ')))
# areaTriangulo(base,altura)



# def calcularImc(p, a):
#     print(p / a **2)
# calcularImc(78,174)

# peso = float(input('Digite seu peso: '))
# altura = float(input('Digite sua altura: '))
# calcularImc(peso, altura)


# def areaTrapezio(bma, bme, a):
#     print((bma + bme) * a /2)
# areaTrapezio(20, 10, 8)

# baseMaior = float(input('Digite a metragem da maior base do trapézio: '))
# baseMenor = float(input('Digite a metragem da menor base do trapézio: '))
# altura = float(input('Digite a metragem da altura do trapézio: '))
# areaTrapezio()

def Velocidade(v):
    if v >50:
        print('A velocidade está acima do limite permitido na via')
    else: 
        print('A velicidade esta dentro do limite permitido na via')
Velocidade(51)

def numeroParOuImpar(x):
    if x %2 == 0:
        print('Esse numero é par!')
    else:
        print('Esse numero é impar')
numero = float(input('Digite um numero: '))
numeroParOuImpar()


def sequenciaNumeros(numero):
    for i in range(numero +1):
        print(i)



def verificarPrimo(numero):
    quantidadeDeDivisores = 0
    for in range(1, numero +1):
        if numero % i == 0:
            quantidadeDeDivisores += 1
    if quantidadeDeDivisores <= 2:
        print(f' O {numero}, é primo')
    else:
        print(f' O {numero}, não é primo')

verificarPrimo(4)
verificarPrimo(5) 
    





        