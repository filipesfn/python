import time
while True:
   numero = int(input("Digite um número inteiro e positivo: "))
   if numero < 0:
    print(f"Digite um número positivo")
    continue
   elif numero == 0:
     break 
   for i in range(numero, -1, -1):
     print(i)
     time.sleep(1)



