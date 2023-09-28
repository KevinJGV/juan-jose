#validar el nombre del usuario 
while True:
    try:
        nombre = input("ingrese el nombre del usuario: ")
        nombre = nombre.strip()
        if len(nombre == 0) == 0 or  nombre.isalnum() == False:
            print("nombre invalido. vuelva a digitarlo")
            continue
        break
    except Exception as e:
        print("Error al ingresar el nombre.\n", )
        
# validar el estrato
while True:
    try:
        estrato = int(input("Ingresa el estrato (1-5)"))
        if estrato <1 or estrato > 5:
            print("El estrato no esta en el rango (1-5). intente de nuevo:")
            continue
        break
    except ValueError:
        print("Error. estrato invalido")
        
if estrato == 1:
    tbas = 10000
elif estrato == 2:
    tbas = 15000
elif estrato == 3:
    tbas = 30000
elif estrato == 4:
    tbas = 50000
elif estrato == 5:
    tbas = 60000
    
print("\n", "=" * 30)
print("Nombre:", nombre)
print("Tarifa básica: ", tbas)