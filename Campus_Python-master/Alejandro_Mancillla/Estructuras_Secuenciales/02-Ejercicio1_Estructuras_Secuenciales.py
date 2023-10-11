print("CALCULADORA PAGO CONDUCTOR\n")

#INGRESO DE DATOS
Conductor = input("Ingrese nombre del Conductor: ")
Placa = input("Ingrese placa del vehiculo: ")
ValorPasajes = float(input("Ingrese el valor total de pasajes: "))
ValorEncomiendas = float(input("Ingrese el valor total de encomiendas: "))

#PROCESO
LiquidacionPasajes = ValorPasajes * 0.25
LiquidacionEncomiendas = ValorEncomiendas * 0.15
TotalPagar = LiquidacionEncomiendas + LiquidacionPasajes

#SALIDA
print(f"\nLIQUIDACIÓN TOTAL \n\tCONDUCTOR: {Conductor} \n\tPLACA: {Placa} \n\tVALOR TOTAL PASAJES: {ValorPasajes} \n\tVALOR A PAGAR PASAJES: {LiquidacionPasajes} \n\tVALOR TOTAL ENCOMIENDAS: {ValorEncomiendas} \n\tVALOR A PAGAR ENCOMIENDAS: {LiquidacionEncomiendas} \n\tVALOR TOTAL A PAGAR: {TotalPagar}")