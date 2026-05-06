numero = 0
soma = 0
qtd = 0

while(numero != -1):
    numero = int(input("Digite o número desejado: "))

    if(numero != -1):
        soma = soma + numero
        qtd= qtd+1

 

media = soma / qtd
print ("A média é: " , media )
