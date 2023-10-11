DiccionarioCategoria = {1: 25000, 2: 30000, 3: 40000, 4:45000, 5: 60000}

TotHonor = 0
Docentes = {}
while True:
    Cedula = int(input("Ingrese cédula del docente: "))
    Nombre = input("Nombre del docente: ")
    Categoria = int(input("Categoria del docente: "))
    Horas = int(input("Horas laboradas en el mes del docente: "))
    Docentes[Cedula] = {}
    Docentes[Cedula]["Nombre"] = Nombre
    Docentes[Cedula]["Categoria"] = Categoria
    Docentes[Cedula]["Horas"] = Horas

    Opc = input("Desea agregar otro docente (S/N)? ")
    if Opc.lower() == "n":
        break

print("\n\n *** INFORME ***")
print("-" * 35)
for i in Docentes.keys():
    Honor = Docentes[i]["Horas"] * DiccionarioCategoria[Docentes[i]["Categoria"]]
    TotHonor += Honor
    print("Docente:",Docentes[i]["Nombre"], f" -- ${Honor:,}")
print("=" * 40)
print(f"Total Honorarios de los docentes: ${TotHonor:,}")