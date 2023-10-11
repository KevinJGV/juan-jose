#FUNCION QUE CALCULE LA MEDIA DE TRES NUMERO

def Media3(N1, N2, N3):
    Media = (N1 + N2 + N3) / 3
    return Media

#Función Validar Entero
def LeerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error! Ingrese un numero entero valido")

a = LeerInt("Ingrese el primer numero: ")
b = LeerInt("Ingrese el segundo numero: ")
c = LeerInt("Ingrese el tercer numero: ")
Prom = Media3(a, b, c)
print(f"La media de {a}, {b} y {c} es {Prom:.3f}")