def menu():
    while True:
        try:
            print("*** NOMINA ACME ***")
            print("        MENU       ")
            print("1. Agrega empleado")
            print("2. Modificar empleado")
            print("3. Buscar empleado")
            print("4. Eliminar empleada")
            print("5. Listar nómina de un empleado")
            print("6. Listar nómina de todos lo empleados")
            print("8. Salir")
            op = input(">> Escoja una opcion (1-8)")
            if op < 1 or op > 5:
                print("Opción no válida. Escoja de 1 a 8.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 8.")
            input("Presione cualquier tecla para continuar...")
    
def leerNum(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            return num
        except ValueError:
            print("Error. Número inválido")
            input("Presione cualquier tecla para continuar...")

def leerNombre(msj):
    while True:
        try:
            nom = input(msj)
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)
    