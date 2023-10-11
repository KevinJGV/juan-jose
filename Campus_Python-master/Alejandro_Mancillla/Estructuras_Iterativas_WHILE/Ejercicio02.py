#NUMEROS PRIMOS
Num = 0
Divisores = 0

while Num >= 0:
    Num = int(input("Ingrese un numero (Negativo para salir): "))
    for i in range(1, Num + 1):
        if Num % i == 0:
            Divisores += 1
    if (Divisores < 3) and Num > 0:
        print(f"El numero {Num} es primo")
    elif (Divisores > 2) and Num > 0:
        print(f"El numero {Num} NO es primo")
    Divisores = 0