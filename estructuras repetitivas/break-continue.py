#break
#calcular si un numero es primo
#num primo: divisible por si mismo y por 1

num = int(input("Ingrese un numero? "))

if num < 2:
    print("No es primo ")
elif num == 2:
    print("Es primo")
else:
    es_primo = True # variables banderas o switch
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
if es_primo == True:
    print("Es primo")
else:
    print("No es primo, lo divide", i)
    
    
#CONTINUE
#salta una iteracion de un ciclo

#imprima los numeros del 1 al 100 excepto los multiplos de 7

for i in range(1, 101):
    if i % 7 == 0:
        continue
    print(i, end=", ")