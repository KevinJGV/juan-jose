#FECHA DE NACIMIENTO
Fecha = input("Ingrese su fecha de nacimiento (DD/MM/AAAA): ")
Fecha = Fecha.split("/")
Dia = ""
Mes = ""
if len(Fecha[0]) == 1:
    Dia = "0" + Fecha[0]
else:
    Dia = Fecha[0]
print(f"Día: {Dia}")
if len(Fecha[1]) == 1:
    Mes = "0" + Fecha[1]
else:
    Mes = Fecha[1]
print(f"Mes: {Mes}")
print(f"Día: {Fecha[2]}")