def sumar (op1,op2,op3):
    return op1+op2+op3

lista= [1,2,3]
x=0

print (lista)

for i in range(3,30):
   suma= sumar(lista[0], lista[1], lista[2])
   #print("Suna int: ", suma)
   suma= str(suma)
   #print("Suma str: ", suma)
   suma= "000" + str(suma)
   #print("Suma str + 000: " ,suma)
   suma= suma[-4:]
   #print ("Suma ultimos 4 lugares: ", suma)
   suma= int(suma)
   #print("Suma int: ", suma)

   if x<3:
       lista[x]= suma
       x= x+ 1
   else:
       x=0
       lista[x]=suma
       x=x+1

print(suma)

