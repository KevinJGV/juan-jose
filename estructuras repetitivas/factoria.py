# calcular el factorial de un numero
# factorial de 5 = 1 * 2 * 3 * 4 * 5 = 120}

n = int(input("numero? "))
fact = 1

for m in range(1, n + 1):
    fact *= m
    
print(f"El factorial de {n} es {fact:,}")