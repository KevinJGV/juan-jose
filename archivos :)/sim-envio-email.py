fd = open("archivos :)/mbox-short.txt", "r")

fd2 = open("archivos :)/envio-emails.txt", "w")

lstEmails = []
for linea in fd:
    if linea.startswith("From:"):
        email = linea.split()[1]
        if email not in lstEmails:
            lstEmails.append(email)

lstEmail = list(lstEmails)
for i in range(len(lstEmail)-1, -1, -1):
    #enviar correo
    msj = f"{lstEmail[i]} enviado [ok]"
    print(msj)
    fd2.write(msj+"\n")
        
fd.close()
fd2.close()