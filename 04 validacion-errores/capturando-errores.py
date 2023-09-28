while True:
    try:
        num1 = int(input("ingrese un numero: "))
        break
    except ValueError:
        print("Error. número entero no válido.")
    
while True:
    try:
        num2 = int(input("ingrese otro numero: "))
        break
    except ValueError:
        print("Error. número entero no válido.")
    

try:
    num2 = "a"
    suma = num1 + num2
    print("la suma es: ", suma)
except Exception as e:
    print("Error al intentar sumar.\n", e )