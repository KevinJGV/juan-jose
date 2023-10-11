print("CALCULAR NUEVA HORA")

#DATOS DE ENTRADA
Horas = int(input("Ingrese la Hora Actual: "))
Minutos = int(input("Ingrese los Minutos Actuales: "))
MinAdicionales = int(input("Ingrese los minutos adicionales: "))

#PROCESO
Horas = Horas + ((Minutos + MinAdicionales)  // 60)
Minutos = (Minutos + MinAdicionales) % 60

#SALIDA
print(f"\n{Horas}:{Minutos}")