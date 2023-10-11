archivo = open("archivos :)/nombres.txt", "r")

texto = archivo.read()
print(texto)

archivo.seek(0) #se indica la posisicion donde quiero que se ubique el puntero
texto2 = archivo.readline() #lee una linea, para no correr riesgo de quedarnos sin memoria
print(texto2)

texto3 = archivo.readlines() # lee toda las lineas
print(texto3)

archivo.close()