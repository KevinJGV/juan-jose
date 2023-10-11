print("CALCULADORA NOTA DEFINITIVA")

#INGRESO DE DATOS
Estudiante = input("Ingrese su nombre: ")
Nota1 = float(input("Ingrese nota del Reto 1: "))
Nota2 = float(input("Ingrese nota del Reto 2: "))
Nota3 = float(input("Ingrese nota del Reto 3: "))
NotaIngles = float(input("Ingrese nota de Ingles: "))

#PROCESO
Definitiva = (Nota1 * 0.2) + (Nota2 * 0.25) + (Nota3 * 0.35) + (NotaIngles * 0.2)

#SALIDA
print(f"\n{Estudiante} su nota definitiva es: {Definitiva} ") 