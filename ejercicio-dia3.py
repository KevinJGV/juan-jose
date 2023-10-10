# ejercicio 1

km_recorridos = float(input("Ingrese la distancia por recorrer "))
dias_De_Estancia = int(input("Ingrese los dias de estancia "))

precio_Km = 0.63 #precio tiquete

total = km_recorridos * dias_De_Estancia

costo_Total_Sin_Reduccion = precio_Km * km_recorridos

if km_recorridos > 7 and dias_De_Estancia > 800:
    reduccion = 0.30 * costo_Total_Sin_Reduccion
else:
    reduccion = 0

costo_Final = costo_Total_Sin_Reduccion - reduccion

print(f"El valor del billete de ida y vuelta es de: %{costo_Final: .2f} USD")

# ejercicio 2

año = int(input("ingrese el año: "))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print(f"{año} es un año bisiesto ")
        else:
            print(f"{año} no es un año bisiesto ")
    else: 
        print(f"{año} es un año bisiesto")
else:
    print(f"{año} no es un año bisiesto")
    
# ejercicio 3

peso_Libras = float(input(f"ingrese su peso en libras "))

altura_Pulgadas = float(input(f"ingrese su altura en pulgadas "))

peso_kilos = peso_Libras * 0.45359237 
altura_metros = altura_Pulgadas * 0.0254

imc = peso_kilos / (altura_metros ** 2)

print(f"Tu IMC es: {imc:.2f}")

#ejercicio 4

hoy = int(input("Ingresa el dia de la semana actual; 0 para domingo, 1 para lunes, 2 para martes, 3 para miercoles, 4 para jueves, 5 para viernes, 6 para sabado: "))

dias_En_El_Futuro = int(input("ingresa el numero de dias al futuro: "))

dia_Futuro = ( hoy + dias_En_El_Futuro) % 7

nombres_Dias = ["domingo", "lunes", "martes", "miercoles", "jueves", "viernes", "sabado"]

print(f"el dia en el futuro sera {nombres_Dias[dia_Futuro]}.")

#ejercicio 5
# muy largo con if

numero = int(input("ingrese un numero entero: "))

if numero >= 1 and numero <= 9:
    print("1")
if numero >= 10 and numero <= 99:
    print("2")
if numero >= 100 and numero <= 999:
    print("3")
if numero >= 1000 and numero <= 9999:
    print("4") 
if numero >= 10000 and numero <= 99999:
    print("5")
if numero >= 100000 and numero <= 999999:
    print("6")
if numero >= 1000000 and numero <= 9999999:
    print("7")   
    
    """ hola """