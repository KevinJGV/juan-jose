def suma(num1, num2):
    resultado = num1 + num2
    return resultado

def resta(num1, num2):
    return  num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        resultado = None
    return resultado  


def menu():
    while True:
        try:
            print("*** MENU CALCULADORA ***")
            print("1. sumar()")
            print("2.restar")
            print("3.multiplicar")
            print("4.dividir")
            print("5.salir")
            op = int(input(">>> opcion (1-5)? "))
            if op < 1 or op > 5:
                print("opcion no valida. escoja de 1 a 5.")
                print("Presiona cualquier tecla para continuar")
                continue
            return op
        except ValueError:
            print("opcion no valida. escoja de 1 a 5.")
            
def leernum(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            return num
        except ValueError:
            print("Error. numero invalido: ")
            input("Presione cualquier tecla para continuar: ")  
                
         
## programa principal

while True:
    opcion = menu()
        
    if opcion == 1:
        print("\n\n1.sumar")
        num1 = leernum("ingrese el primer numero: ")
        num2 = leernum("ingrese el segundo numero: ")
        print(f"El resultado de la suma es: {suma(num1, num2):.3f}")        
    elif opcion == 2:
        print("\n\n1.restar")
        num1 = leernum("ingrese el primer numero: ")
        num2 = leernum("ingrese el segundo numero: ")
        print(f"El resultado de la resta es: {resta(num1, num2):.3f}")
    elif opcion == 3:
        print("\n\n1.multiplicar")
        num1 = leernum("ingrese el primer numero: ")
        num2 = leernum("ingrese el segundo numero: ")
        print(f"El resultado de la multiplicacion es: {multiplicacion(num1, num2):.3f}")
    elif opcion == 4:
        print("\n\n1.dividir")
        num1 = leernum("ingrese el primer numero: ")
        num2 = leernum("ingrese el segundo numero: ")
        res = division(num2, num2)
        if res != None:
            print(f"El resultado de la division es: {division(num1, num2):.3f}")
        else:
            print("Division entre cero es indeterminada. ")    
    elif opcion == 5:
        print("\n\nGracias por usar la calculadora")
        print("adios")
        input("Presione cualquier tecla para salir  ... ")
        break
    input("presione cualquier tecla para volver al MENU ... ")