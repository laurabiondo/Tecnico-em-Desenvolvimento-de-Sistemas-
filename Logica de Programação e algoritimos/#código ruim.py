#CLEAN CODE 1
nota1 = float(input("Digite a primeira nota:"))
nota2 = float(input("Digite a segunda nota:"))
nota3 = float(input("Digite a terceira nota:"))
nota4 = float(input("Digite a quarta nota:"))

media = (nota1 + nota2 + nota3 + nota4)/ 4

print ("Sua média é: ", media)

if (media >= 7):
    print ("APROVADO 🎉")

elif (media  >= 5):
    print ("RECUPERAÇÃO 😵")

elif (media < 5):
    print ("REPROVADO 😭")

else:
    print ("INVÁLIDO ❌")

#Clean code 2

notas = []

for i in range(4):
    notas.append(float(input(f"Digite a {i+1}ª nota: ")))

media = sum(notas)/len(notas)

print ("Sua média é: ", media)

if (media >= 7):
    print ("APROVADO 🎉")

elif (media  >= 5):
    print ("RECUPERAÇÃO 😵")

elif (media < 5):
    print ("REPROVADO 😭")

else:
    print ("INVÁLIDO ❌")
