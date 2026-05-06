numeros = []
maior = -99999999999999999999
for i in range(5):
    numeros.append(int(input("Digite os números: ")))

for numero in numeros:
    if(numero > maior):
        maior = numero


print ("O maior número é: ", maior)