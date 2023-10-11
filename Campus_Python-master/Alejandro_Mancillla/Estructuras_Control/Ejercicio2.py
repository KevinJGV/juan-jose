Horas = int(input("Ingrese la Hora: "))
Minutos = int(input("Ingrese los Minutos: "))
Segundos = int(input("Ingrese los Segundos: "))
AP = input("AM/PM: ")

if AP == "AM":
    if Horas == 12:
        Horas = 0
else:
    if Horas == 12:
        Horas = 12
    else:
        Horas = Horas + 12

print("\n")
print(f"{Horas:02d}:{Minutos:02d}:{Segundos:02d}")