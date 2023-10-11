#VERIFICAR SI UN NUMERO DADO ES PERFECTO
Num = int(input("\nIngrese numero a evaluar: "))
Cont = 1
Acumulador = 0

#Buscar Divisores hasta Num-1
while Cont < Num:
    if Num % Cont == 0:
        Acumulador += Cont
    Cont += 1

#Comparar y evaluar si es perfecto
print("-" * 35)
if (Acumulador == Num):
    print(f"El numero {Num} es Perfecto")
else:
    print(f"El numero {Num} NO es perfecto")
print("-" * 35)