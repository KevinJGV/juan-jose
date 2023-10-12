archivo = open("archivos :)/mbox.short.txt", "r")
cp = 0
n = 0
#for linea in archivo:    #contar linea por linea
#    n += 1
for linea in archivo:
    linea.strip()
    #cp += len(linea.split(" "))
    for lin in linea.split(""):
        if lin.isalnum():
            cp +=1

archivo.close()

print(f"cantidad de palabras {cp} ")