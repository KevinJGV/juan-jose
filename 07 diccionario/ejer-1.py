def calcularnotaDefinitiva(nota1, nota2, nota3):
    nota1peso = nota1 * 0.30
    nota2peso = nota2 * 0.30
    nota3peso = nota3 * 0.40
    notaDefinitiva = nota1peso + nota2peso + nota3peso
    return notaDefinitiva

def determinarAprobacion(nota):
    if nota >= 3.0:
        return "Aprobado"
    else:
        return "Reprobado"

estudiantes = {}

while True:
    codigo = input("Ingrese el código del estudiante (999 para salir): ")
    if codigo == "999":
        break
    
    nombre = input("Ingrese el nombre del estudiante: ")
    nota1 = float(input("Ingrese la nota 1: "))
    nota2 = float(input("Ingrese la nota 2: "))
    nota3 = float(input("Ingrese la nota 3: "))
    
    notaDefinitiva = calcularnotaDefinitiva(nota1, nota2, nota3)
    resultado = determinarAprobacion(notaDefinitiva)
    
    estudiantes[codigo] = {
        "Nombre": nombre,
        "Nota 1": nota1,
        "Nota 2": nota2,
        "Nota 3": nota3,
        "Nota Definitiva": notaDefinitiva,
        "Resultado": resultado
    }

for codigo, datos in estudiantes.items():
    print(f"Código: {codigo}")
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")
    print("\n")