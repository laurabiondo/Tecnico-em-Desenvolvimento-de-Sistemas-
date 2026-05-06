l1 = int(input("Digite o primeiro número:"))
l2 = int(input("Digite o segundo número:"))
l3 = int(input("Digite o terceiro número:"))

if ((l1 + l2) > l3 and (l1+ l3) > l2 and (l2+l3) > l1):
    if(l1 == l2 and l2 == l3 and l3 == l1):
       print ("EQUILÁTERO")

    elif (l1!= l2 and l2 != l3 and l3 != l1):
        print ("ESCALENO")

    else: 
        print ("Isóceles")

else: 
   print ("inválido")