#SINTAXIS GENERAL
#def NombreFuncion([Param1, Param2, Param3, etc]):
    #Cuerpo = Instrucciones

#Funcion Sumar 2 Numeros
def Suma2(Num1, Num2):
    Suma = Num1 + Num2
    return Suma

def LeerInt(msg):
    while True:
        try:
            n = int(input(msg))
            return n
        except ValueError:
            print("Error! Ingrese un numero entero valido")

a = LeerInt("Ingrese un numero Entero: ")
b = LeerInt("Ingrese otro numero Entero: ")
print("La suma de los numeros es:", Suma2(a, b))