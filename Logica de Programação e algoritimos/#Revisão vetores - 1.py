#Revisão vetores - 1
#preencher o vetor 
#percorrer o vetor e calcular a soma dos números 
#exibir a soma 
#----------------------------------------------------------------------------------------------
#Passo 1) criar as variaveis

qtd = int(input("Digite a quantidade de números: "))
vetor = []
soma = 0

#passo 2) Preencher o vetor 
for i in range (qtd):
    vetor.append (int(input("Digite um número: ")))

#Passo 3)Percorrer o vetor 
for num in vetor: 
    soma = soma + num 

print ("A soma é: ", soma )