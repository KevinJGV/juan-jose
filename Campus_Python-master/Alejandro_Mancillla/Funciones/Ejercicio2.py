#SERVICIO ENERGÍA ELECTRICA, SEGÚN ESTRATO 

#Función Leer String
def LeerString(msg):
    while True:
        try:
            Name = input(msg)
            if Name.strip() == "":
                print("Error. Ingrese un nombre valido")
                input("Digite cualquier tecla para continuar")
                continue
            return Name
        except Exception as e:
            print("Error al ingresar el nombre.", e.message)

#Función Validar Entero dentro del estrato valido
def LeerEstrato(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 1 or n > 5:
                print("Opción no valida")
                input("Digite cualquier tecla para continuar")
                continue
            else:
                return n
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#Función Calcular el valor de la tarifa Basica
def CalcularTarifa(Est):
    if Est == 1:
        Basica = 10000
    elif Est == 2:
        Basica = 15000
    elif Est == 3:
        Basica = 30000
    elif Est == 4:
        Basica = 50000
    elif Est == 5:
        Basica = 65000
    return Basica

#Codigo Principal
Nombre = LeerString("\nIngrese el nombre del Usuario: ")
Estrato = LeerEstrato("Ingrese el estrato del Usuario: ")
Tarifa = CalcularTarifa(Estrato)
print(f"\nLa tarifa del Usuario {Nombre} es = ${Tarifa:,}")

