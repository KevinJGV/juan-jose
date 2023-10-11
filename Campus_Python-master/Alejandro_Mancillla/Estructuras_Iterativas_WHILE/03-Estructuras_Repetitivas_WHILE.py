Frase = input("Ingrese una frase: ")
Frase = Frase.lower()
Longitud = len(Frase)
Contador = 0
Vocales = 0

while Contador < Longitud:
    if(Frase[Contador] == "q"):
        break
    if Frase[Contador] in "aeiou":
        Vocales += 1
    Contador += 1

print(f"\nLa frase Ingresada tiene {Vocales} vocales")