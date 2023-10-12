fd = open("archivos :)/mbox-short.txt", "r")
fd2 =  open("archivos :)/resultado-simu-exe.txt", "w")

setEmail = set()
for linea in fd:
    if linea.startswith("To:"):
        setEmail.add(linea.split()[1])

for correo in setEmail:
    fd2.writelines([f"{correo} sent [ok]"])

fd2.close()
fd.close()