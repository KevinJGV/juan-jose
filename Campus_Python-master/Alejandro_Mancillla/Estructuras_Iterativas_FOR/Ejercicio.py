# #IMPRIMIR NUMEROS PARES DE 1 A 100
# for i in range(1,101,1):
#     if i % 2 ==0:
#         print(i, end=", ")

# #CALCULAR FACTORIAL DE UN NUMERO
# Num = int(input("Ingrese numero a calcular: "))
# Fact = 1
# for i in range(1,Num+1 ,1):
#     Fact = Fact * i
# print(f"{Num}! = {Fact}")

#CALCULAR NUMERO PRIMO O NO
Num = int(input("Ingrese numero a calcular: "))
Div = 0
for i in range(1,Num+1):
    if Num % i == 0:
        Div = Div + 1
if Div == 2:
    print(f"{Num} no es primo")
else:
    print(f"{Num} es primo")