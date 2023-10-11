#MAYOR Y MENOR
Num = 0
May = 0
Cont = 1

while Num >= 0:
    Num = int(input("\nIngrese un numero (Negativo para salir): "))
    if Cont == 1:
        Men = Num
    if Num > May:
        May = Num
    elif Num < Men and Num >= 0:
        Men = Num
    Cont += 1

print("-" * 35)
print(f"El numero menor fue {Men}")
print(f"El numero Mayor fue {May}")
print("-" * 35)
