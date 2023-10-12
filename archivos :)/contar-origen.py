# un programa que cuente y muestre los correos de origen distintos que hay en el mbox.txt
#def miFun(email)
    #return len(email)
fd = open("archivos :)/mbox.short.txt", "r")
#cl = 0
setEmail = set()
for linea in fd:
    if linea.startswith("from"):
        #cl += 1
        #email = linea.split()[1]
        #print(email)
        setEmail.add(linea.split()[1])
        
        
fd.close()
cl = len(setEmail)
print("cantidad de correos de origen distintos: ", cl)
for email in sorted(setEmail, reverse=False, key=lambda x:len(x)): #o se  puede hacer con funcion
    print(email)