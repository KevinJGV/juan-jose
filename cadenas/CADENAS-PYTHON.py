s = "yo soy tu padre"
# print(s[7])
# print(s[-8])

# #recorrer las cadenas
# for i in range(len(s)):
#     print(s[i], end=", ")
    
# # RECORRIDO POR ELEMENTO
# print("")
# for e in s:
#     print(e, end=", ")
    
# # slice = porcion
# print("")
# print(s[2:])
# print(s[4: 7])
# print(s[::-1])

#recorrer un string
#para recorrer un string tambien podemos utilizar el comando for(que es una alternativa a usar whiles).

#s = input("ingrese string")
#for i in 

#operador in
#print("tu" in s)
#print("yt" not in s)

#upper() VUELVE MAYUS
"Hola Mundo".upper()

#LOWER() VUELVE MINUS

#capitlize() solo la primera mayus

#title() primer letra de cada palabra mayus

#count()
print(s.count("o"))

#find() encuentra subcadena en otra y devulve donde aparece
print(s.find("pa"))

#rfind devuelve el indice en el que aparece la subcadena; empezando por el final
"hola mundo mundo mundo".rfind('mundo') 

#isdigit() devuelve true si cadena de numeros
snum = "100"
print(snum.isdigit())
snum = "100a"
print(snum.isdigit())

#isalnum() devulve true si la cadena es todo numeros o todos letras
c = "ABC100034po"
c.isalnum()

#isalpha() devuelve si la cadena son solo letras

c = "ABC100034po"
c.isalpha

#islower() devuelve true si la cadena es todo minusculas
"hola mundo".istitle()

# istitle() devuelve true si las letras son minusculas

#isspace() devuelve true si la cadena es todo espacios
" - ".isspace

#starswith() devuelve true si las cadena empieza con una subcadena
"hola mundo".endswith('mundo')

#endswith() devuelve si la cadena termina con una subadena o palabra especifica

#split() separa la cadena en subcadenas a partit de sis espacios y devuelve una lista
nombre = "juan jose navarro hernandez"
email = "juanjose10404@gmail.com"
miles = "1.215.254"
print(nombre.split())
print(nombre.split("jose"))
print(email.split("@"))
print(miles.split("."))

#join() une todos los caracteres de una cadena urtilizando un caracter de union

",".join("hola mundo")

#strip() borra todos los espacio por delante y detras de una cadena y la devuelve

"    hola mundo    ".strip()

#podemos indicar el caracter a borrar

#replace reempalaza una subcadena de uan por otra y la devuelve:
"Hola Mundo".replace('o','0')
