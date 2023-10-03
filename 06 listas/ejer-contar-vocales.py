letras = []
while True:
    letra = input("Ingrese una letra del abecedario:  ")
    if not letra.isalpha():
        print(">> Error. Letra no válida\n")
        input()
        continue
        
    letras.append(letras)
    
    op = input("\nDesea continuar (S\\N)? ")
    if op.lower() != "s" :
        break
        
print("\n", "=" * 30)
vocales = ["a", "e", "i", "o", "u"]
canVocales = [0] * 5
print(canVocales)

# recorer la lista por elementos

for l in letras:
    if l.lower in vocales:
        p = vocales.index(l.lower()) #INDEX = ENCONTRAR-BUSCAR
        canVocales[p] += 1
        
#recorrido por posicion

for p in range(len(vocales)):
    print(vocales[p], " = ",canVocales[p])