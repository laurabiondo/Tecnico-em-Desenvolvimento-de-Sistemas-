positivo = 0 
negativo = 0 
for i in range(10):
    numero = int(input("Digite um número: "))

    if numero < 0:
        print ("O número é negativo")

    elif numero > 0: 
        print ("O número é positivo ")

    else: 
        print("Inválido")
