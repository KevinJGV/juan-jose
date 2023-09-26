# punto 1
print("ejercicio 1")
print("*\n")
print("**\n")
print("****\n")
print("*****\n")

#numero 2
print("ejercicio 2")
print("*********")
print("*\t*")
print("*\t*")
print("*\t*")
print("*********\n")

# Definir constantes, punto 3
print("ejercicio 3")
valor_hora_de_trabajo = 20000
eps_porcentaje = 0.04
valor_pension = 0.04
horas_trabajadas = 150
sueldo_bruto = 3000000
sueldo_neto_total = 2999999.92
sueldo_neto = ("sueldo_bruto - eps_porcentaje - valor_pension ")
print(valor_hora_de_trabajo * horas_trabajadas)

print(f"valor hora de trabajo: {valor_hora_de_trabajo}")
print(f"eps_porcentaje: {eps_porcentaje}")
print(f"valor de la pension: {valor_pension}")
print(f"horas de trabajo: {horas_trabajadas}")
print(sueldo_bruto - eps_porcentaje - valor_pension)
print(f"sueldo bruto: {sueldo_bruto}")
print(f"sueldo neto: {sueldo_neto_total}")

# punto 4
print("ejercicio 4")

# Obtener la cantidad de segundos desde el usuario
segundos = int(input("ingrese los segundos"))

# calcular horas, minutos y segundos

horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

# Mostrar el resultado
print(f"{horas} horas")
print(f"{minutos} minutos")
print(f"{segundos} segundos")

# punto 5
print("ejercicio 5")
# Obtener la nota como un número de punto flotante
nota = float(input("Ingrese la nota (de 0.0 a 5.0): "))

# Verificar si la nota está en el rango válido de 0.0 a 5.0
if nota < 0.0 or nota > 5.0:
    print("La nota debe estar en el rango de 0.0 a 5.0")
else:
    # Calcular la curva de 8
    curva_de_ocho = nota * 0.8 + 1.0
    
    # Mostrar el resultado con dos decimales
    print(f"La curva de 8 de la nota {nota:.2f} es {curva_de_ocho:.2f}")
