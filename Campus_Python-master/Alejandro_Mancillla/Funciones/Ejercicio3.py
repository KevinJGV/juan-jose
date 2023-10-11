#LIQUIDAR MATRICULA ESTUDIANTE, SEGÚN PROGRAMA Y TIPO DE BECA

#Función Mensaje Error
def MsgError(msg):
    print(" ERROR!", msg)
    input(" Presione cualquier letra para regresar al Menú")

#Función Validar Entero
def LeerInt(msg):
    while True:
        try:
            n = int(input(msg))
            if n > 0:
                return n
        except ValueError:
            print("Error! Ingrese un numero entero valido")

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

#Menú para elegir Programa Académico
def MenuPrograma():
    while True:
        print("\n*********")
        print(" PROGRAMAS ACADÉMICOS")
        print("\t1. Técnico en Sistemas")
        print("\t2. Técnico en Desarrollo de videojuegos")
        print("\t3. Técnico en Animación Digital")
        try:
            Opc = int(input("Elija un programa: "))
            if Opc < 1 or Opc > 3:
                MsgError("Opción no valida")
                continue
            else:
                return Opc
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#Menú para elegir Programa Académico
def MenuBeca():
    while True:
        print("\n*********")
        print(" INDICADOR DE BECA")
        print("\t1. Beca por Rendimiento académico")
        print("\t2. Beca Cultural")
        print("\t3. Sin Beca")
        try:
            Opc = int(input("Elija un programa: "))
            if Opc < 1 or Opc > 3:
                MsgError("Opción no valida")
                continue
            else:
                return Opc
        except ValueError:
            print("Error! Ingrese un numero entero valido")

#Funcion Calcular Valor Neto
def CalcularMatricula(Pro, Bec):
    if Bec == 1:
        Desc = 0.5
    elif Bec == 2:
        Desc = 0.4
    elif Bec == 3:
        Desc = 0

    if Pro == 1:
        Valor = 800000
    elif Pro == 2:
        Valor = 1000000
    elif Pro == 3:
        Valor = 1200000
    
    Neto = Valor - (Valor * Desc)
    return Neto

Codigo = LeerInt("\nIngrese el Codigo del Estudiante: ")
Nombre = LeerString("Ingrese el Nombre del Estudiante: ")
Programa = MenuPrograma()
Beca = MenuBeca()
ValorNeto = CalcularMatricula(Programa, Beca)

print("-" * 45)
print("LIQUIDACIÓN MATRICULA ESTUDIANTE")
print(f"Estudiante: {Nombre}")
print(f"Valor a pagar: ${ValorNeto:,.0f}")
