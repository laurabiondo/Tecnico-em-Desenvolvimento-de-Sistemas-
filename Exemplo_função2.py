# Criando função 
def calcularMedia(nota1, nota2, nota3, nota4):
    media = nota1+nota2+nota3+nota4/4
    print("Sua média é", media)

# Chamando função para o primeiro aluno
calcularMedia(4.5,7,8,6)

# Chamando função para o segundo aluno 
n1 = int(input("Digite a nota 1: "))
n2 = int(input("Digite a nota 2: "))
n3 = int(input("Digite a nota 3: "))
n4 = int(input("Digite a nota 4: "))

calcularMedia(n1,n2,n3,n4)