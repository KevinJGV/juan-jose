# ejemplos de formatear la salida

# CON FORMAT
sueldo= 5600000
print("sueldo: ${:,}".format(sueldo))

interes = 4352.2345234523
print("valor del interes: {:,.3f}".format(interes))

# f-string
print(f"sueldo: ${sueldo:,}")