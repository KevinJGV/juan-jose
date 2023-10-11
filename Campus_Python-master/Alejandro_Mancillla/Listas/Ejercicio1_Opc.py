lstLetras = []
Cadena = input("Ingrese cadena: ")
for i in range(len(Cadena)):
    lstLetras.append(Cadena[i])
print(lstLetras)

ctA = lstLetras.count("a")
print(f"Hay {ctA} letras a en la lista")
ctE = lstLetras.count("e")
print(f"Hay {ctE} letras e en la lista")
ctI = lstLetras.count("i")
print(f"Hay {ctI} letras i en la lista")
ctO = lstLetras.count("o")
print(f"Hay {ctO} letras o en la lista")
ctU = lstLetras.count("u")
print(f"Hay {ctU} letras u en la lista")