def calcular_area_retangulo(b,a):
    return b*a

base = float(input("Digite o comprimento da base do retângulo: "))
altura = float(input("Digite o comprimento da altura do retângulo: "))

area = calcular_area_retangulo(b=base,a=altura)
print(f"A área do retângulo e {area:.2f}")