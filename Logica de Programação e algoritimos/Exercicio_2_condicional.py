idade = int(input("Digite sua idade: "))

if (idade >=0 and idade <=12):
    print ("CRIANÇA🧒")

elif (idade >=13 and idade <=17):
    print ("ADOLESCENTE🧑")
    
elif (idade >=18 and idade <=59):
    print ("ADULTO🧑")

elif (idade >= 60):
    print ("IDOSO🧓")

else: 
   print ("ERRO")