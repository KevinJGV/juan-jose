Nombre = input("Nombre del empleado: ")
Salario = int(input("Salario del empleado:"))

if Salario <= 1200000:
    Subsidio = 120000
else:
    Subsidio = 0
print("\n","-" * 30)
print(f"Empleado= {Nombre} \nSalario= {Salario} \nSubsidio= {Subsidio}")
print("-" * 30, "\n")