# num = int(input("ingrese un numero "))
# cpares = 0
# cimpares = 0
# while num != -1:
#     if num % 2 == 0:
#         print("El numero es par")
#         cpares  += 1
#     else:
#         print("El numero es impar")
#         cimpares += 1 
    
#     num = int(input("ingrese un numero: "))
# print("\n", "=" * 30)
# print("cantidad de numeros pares es: ", cpares)
# print("cantidad de numeros inpares es: ", cimpares)

# #ejercicio recibo de luz

n = True

e1 = 10000
e2 = 15000
e3 = 30000
e4 = 50000 
e5 = 65000

while n == True:
    print(f"\nDatos del ususario ")
    nom = input("nombre: ")
    estr = int(input("Estrato [1 al 6]"))
    
    if estr == 1:
        print("\tNombre: ", nom)
        print(f"\tvalor tarifa basica: &{e1:,}")
        print("\n", "=" * 40)
    if estr == 2:
        print("\tNombre: ", nom)
        print(f"\tvalor tarifa basica: &{e2:,}")
        print("\n", "=" * 40)
    if estr == 3:
        print("\tNombre: ", nom)
        print(f"\tvalor tarifa basica: &{e3:,}")
        print("\n", "=" * 40)
    if estr == 4:
        print("\tNombre: ", nom)
        print(f"\tvalor tarifa basica: &{e4:,}")
        print("\n", "=" * 40)
    if estr == 5:
        print("\tNombre: ", nom)
        print(f"\tvalor tarifa basica: &{e5:,}")
        print("\n", "=" * 40)
  
    cont = input("Desea continuar? \n(S/N)")
    if cont == "s" or cont == "s":
        n = True
        print("\n", "=" * 40)
    elif cont == "n" or cont == "n":
        n = False
        
