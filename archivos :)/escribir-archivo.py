archivo = open("archivos :)/salas.txt", "w")

archivo.write("sputnik\n\t")
archivo.write("apolo\n")

archivo.writelines(["houston\n", "artemis\n"])

archivo.close