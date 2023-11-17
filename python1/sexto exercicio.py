numero1 = float(input("Digite um número: "))
numero2 = float(input("Digite um segundo número: "))

operação = int(input("Digite 1 para somar; 2 - subtrair; 3 para multiplicar ; 4 para dividir."))

if operação == 1:
    resultado = numero1 + numero2
    print(f"{resultado}")

elif operação == 2:
    resultado = numero1 - numero2
    print(f"{resultado}") 

elif operação == 3:
    resultado = numero1 * numero2
    print(f"{resultado}") 

elif operação == 4:
    resultado = numero1 / numero2
    print(f"{resultado}") 

if resultado > 0:
    print(f"Esse número é positivo")
elif resultado = 0:
    print("Esse número é neutro")
else:
    print(f"Esse número é negativo")

if resultado % 2 == 0:
    print(f"Esse número é par")
else:
    print(f"Esse número é impar") 




