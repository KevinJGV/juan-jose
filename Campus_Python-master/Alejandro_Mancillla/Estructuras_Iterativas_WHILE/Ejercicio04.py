#NOTAS ESTUDIANTES
Nomb = ""
Nota = 0
NombMayNota = ""
MayNota = 0
NombMenNota = ""
MenNota = 0
Acumulador = 0 
Cont = 0
Prom = 0

while Nomb != "FIN":
    Nomb = input("\nNombre del Estudiante: ")
    if(Nomb != "FIN"):
        Nota = float(input("Nota del Estudiante: ")) 
        if Cont == 0:
            MenNota = Nota
        if Nota > MayNota:
          NombMayNota = Nomb
          MayNota = Nota
        if Nota <= MenNota:
            NombMenNota = Nomb
            MenNota = Nota
        Acumulador += Nota  
        Cont += 1
    
Prom = Acumulador / Cont

#Salida de Datos
print("-" * 45)
print("ESTADISTICAS DEL GRUPO")
print(f"El promedio del curso fue = {Prom:.03f}\n")
print("MENOR NOTA")
print(f"\tNombre = {NombMenNota}")
print(f"\tNota = {MenNota}")
print("MAYOR NOTA")
print(f"\tNombre = {NombMayNota}")
print(f"\tNota = {MayNota}")