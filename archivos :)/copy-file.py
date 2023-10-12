#sirve para copiar en un nuevo archivo txt.
fd = open("archivos :)/nombres.txt", "r") 

fd2 = open("archivos :)/nombres-bak.txt", "w")

for linea in fd:
    fd2.write(linea)


fd2.close()
fd.close()

print("proceso terminado")