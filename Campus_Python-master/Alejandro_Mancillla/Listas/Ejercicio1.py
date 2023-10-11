#CONTAR VOCALES POR SEPARADO DE UNA LISTA

#Funcion Leer Letra
def LeerCaracter(msg):
    while True:
        try:
            n = input(msg)
            if ord(n) < 97 or ord(n) > 122:
                print("Caracter no válido")
                input("Digite cualquier tecla para continuar...")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un caracter válido")
    return

#Función Validar Entero
def LeerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n > 0:
                return n
        except ValueError:
            print("Error! Ingrese un numero entero valido")


lstLetras = []
Num = LeerInt("Cantidad de Letras: ")
for i in range (0, Num):
    Letra = LeerCaracter("Ingrese una letra (Minuscula): ")
    lstLetras.append(Letra)

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