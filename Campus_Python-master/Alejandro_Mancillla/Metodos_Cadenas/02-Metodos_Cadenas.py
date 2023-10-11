#PALABRA PALÍNDROMA
Palabra = input("\nIngrese una palabra: ")
Palabra = Palabra.lower()
Longitud = len(Palabra)
Pal = True
for i in range(0, Longitud):
    if Palabra[i] == Palabra [-(i + 1)]:
        continue
    else:
        Pal = False
        break

if Pal == True:
    print("La palabra ingresada es PALÍNDROMA")
else:
    print("La palabra ingresada NO es PALÍNDROMA")