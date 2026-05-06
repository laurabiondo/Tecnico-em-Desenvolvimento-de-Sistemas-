#Criando uma variavel numérica 
numero = 10 

#Criando uma variável textual 
nome = "Laura"

#Usuário inserir texto 
nome_completo = input("Digite seu nome completo: ")

#Usuário inserir um número inteiro 
idade = int(input("Digite sua idade: "))

#Usuário inserir um número decimal 
salario = float(input("Digite seu salário: "))

#Estruturas condicionais -IF
if (salario >1500 and idade >18):
    print("Você pode tirar carta!: ")
elif (salario <1500 or idade <18):
    print ("Você não pode tirar carta! ")
else:
    print ("Inválido!")

#Estruturas condicionais exemplo 2 
turno = input("Digite seu turno (M/V/N): ")
if (turno == "M"):
    print ("Bom dia! ☀️")
elif (turno == "V"):
    print ("Boa tarde! ☕")
elif (turno == "N"):
    print ("Boa noite! 🌑")
else: #else não tem parêntese
    print("Inválido!")

#Estruras de repetição 
#0-> 10
for i in range (11): #tem que colocar +1
    print(i)

#1 -> 15 
for i in range (1, 16):
    print (i)

#5 -> 65 (aumentando de 5 em 5 )
for i in range (5,66, +5):
    print (i)

#122 -> 0 (tirando de 2 em 2)
for i in range (122, -1,-2):
    print (i)

#Usuário escolhe início e fim 
#início ->fim
inicio = int (input("Início: "))
fim = int (input("Fim: "))

for i in range (inicio, fim+1):
    print (i)

#vetores 
nomes = []
#sempre utilizar para preencher o vetor 
for i in range (5):
    nomes.append(input("Digite um nome: "))
#sempre utilizar para exibir o vetor 
for nome in nomes:
    print (nome) 
