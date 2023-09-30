def calcularFactorial(num):
    factorial = 1
    for i in range(1,num+1):
        mul = i
        factorial = factorial* mul
    return factorial

def readNum(smjNum):
    numero = int(input(smjNum))
    return numero
    
def calcSalario(horas_Trabajadas,valorHora):
    if horas_Trabajadas > 40:
        salario = (40 * valorHora) + ((horas_Trabajadas - 40) * valorHora)
        return salario
    elif horas_Trabajadas <= 40:
        salario = horas_Trabajadas * valorHora
        return salario
    
def cantHoras(msjHoras):
    while True:
        try:
            horas = int(input(msjHoras))
            return horas
        except ValueError:
            print("Numero invalido. D")

def valHora(smjValor):
    while True:
        try:
            valHora = float(input(smjValor))
            return valHora
        except ValueError:
            print("Error.Formato incorrecto. (use el simbolo .)")

def contPalabras(smjText):
            
            parrafo = input(smjText)
            parrafo = parrafo.strip()
            parrafo = parrafo.split(" ")
            cantidadPalabras = len(parrafo)
            return(cantidadPalabras)
    
def menu():
    while True:
        try:
            print("\n")
            print("***** MENÚ *****")
            print("1. Factorial de un número")
            print("2. Calcular el salario de un empleado")
            print("3. Calcular las palabras de un párrafo")
            print("4. Salir")
            op = int(input(">>> Opción (1-5)? "))
            if op < 1 or op > 4:
                print("Rango incorrecto. DIgite un numero entre el 1 y el 4 ")
                input("Presione cualquier tecla para intentar de nuevo... ")
                continue
            return op
        except ValueError:
            print("Opcion no valida. Digite del 1 al 4 ")
            input("Presiones cualquier tecla para intentar de nuevo... ")

op = menu()
while True:
    if op == 2:
        print("\n2. Calcular salario de un empleo")
        horas = cantHoras("Ingrese la cantidad de horas laboradas: ")
        valor = valHora("Ingrese el valor de la hora: ")
        print(f"EL salario del empleado es: {calcSalario(horas, valor):,.2f}")
    elif op == 1:
        print("\n1. Factorial de un numero")
        numero = readNum("Ingrese numero para sacar el Factorial: ")
        b = calcularFactorial(numero)
        print(f"El factorial del numero {numero} es {b}")
    elif op == 3:
        print("\n3. Calcular palabras de un párrafo")
        parrafo = contPalabras("Ingrese el parrafo: ")
        print(f"La cantidad de palabras en el parrafo es: {parrafo}")
    elif op == 4:
        print("Gracias por usar mi programa <3.")
        input("Presione cualquier tecla para salir...")
        break
