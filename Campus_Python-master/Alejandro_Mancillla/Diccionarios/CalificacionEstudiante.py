def MsgNotify(msg):
    print("Notify!",msg)
    input("Presione cualquier tecla para continuar")

def LeerNota(msg):
    while True:
        try:
            Nota = float(input(msg))
            if Nota < 0 and Nota > 5:
                MsgNotify("Nota no Válida")
                continue
            return Nota
        except TypeError:
            print("Ingrese solo numeros")

def LeerCodigo():
    while True:
        try:
            Codigo = int(input("Ingrese codigo del estudiante: "))
            if Codigo <= 0:
                MsgNotify("Codigo no válido")
                continue
            return Codigo
        except TypeError:
            print("Dato no válido")

def CalcularNotas(dcc):
    for i in Estudiantes.keys():
        NotaFinal = (Estudiantes[i]["Nota1"] * 0.3) + (Estudiantes[i]["Nota2"] * 0.3) +(Estudiantes[i]["Nota3"] * 0.4)
        dcc[i]["Final"] = NotaFinal
        if NotaFinal >= 3.0:
            dcc[i]["Estado"] = "APROBADO"
        else:
            dcc[i]["Estado"] = "REPROBADO"
    return dcc

Estudiantes = {}
while True:
    Codigo = LeerCodigo()
    if Codigo == 999:
        break
    Nombre = input("Nombre del Estudiante: ")
    Nota1 = LeerNota("Ingrese la Nota 1: ")
    Nota2 = LeerNota("Ingrese la Nota 2: ")
    Nota3 = LeerNota("Ingrese la Nota 3: ")
    Estudiantes[Codigo] = {}
    Estudiantes[Codigo]["Nombre"] = Nombre
    Estudiantes[Codigo]["Nota1"] = Nota1
    Estudiantes[Codigo]["Nota2"] = Nota2
    Estudiantes[Codigo]["Nota3"] = Nota3
    Estudiantes = CalcularNotas(Estudiantes)

print("\n\n *****     INFORME ESTUDIANTES        *****")
print("-" * 60)
for i in Estudiantes.keys():
    print("Estudiante:",Estudiantes[i]["Nombre"], "-- Nota Final:",Estudiantes[i]["Final"], "-- Estado:",Estudiantes[i]["Estado"])
print("=" * 60)