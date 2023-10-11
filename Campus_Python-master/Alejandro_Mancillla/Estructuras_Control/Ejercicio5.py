#FECHA DEL DÍA SIGUIENTE
print("CALCULAR FECHA DÍA SIGUIENTE\n")

#DATOS DE ENTRADA
Año = int(input("Ingrese el Año (AAAA): "))
Mes = int(input("Ingrese el Mes (MM): "))
Dia = int(input("Ingrese el Día (DD): "))

DiasMes = 0

#PROCESO
if Mes == 1 or Mes == 3 or Mes == 5 or Mes ==7 or Mes == 8 or Mes == 10 or Mes == 12:
    DiasMes = 31
elif Mes == 4 or Mes == 6 or Mes ==9 or Mes == 11:
    DiasMes = 30
else:
    if Año % 4 == 0 and (Año % 100 != 0 or Año % 400 == 0):
        DiasMes = 29
    else:
        DiasMes = 28

Dia = Dia + 1
if Dia > DiasMes:
    Dia = 1
    Mes = Mes + 1
if Mes > 12:
    Mes = 1
    Año = Año + 1

print("\n","-" * 30)
print("Fecha del Día Siguiente")
print(f"{Año:04d} - {Mes:02d} - {Dia:02d}")
print("-" * 30,"\n")