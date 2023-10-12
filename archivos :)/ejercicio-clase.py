ed = open("archivos :)/mbox-short.txt", "r")

setEmail = set()
for linea in ed:
    if linea.startswith("To:"):
        
        setEmail.add(linea.split()[1])
        
        
ed.close()
cl = len(setEmail)
print("cantidad de correos de origen distintos: ", cl)
for email in sorted(setEmail, reverse=False, key=lambda x:len(x)): 
    print(f"{email} enviado [ok]")