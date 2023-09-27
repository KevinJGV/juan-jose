#ejercicio 3
# escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el dia, el mes y el año. adaptar el programa anterior para qu etambien funcione cuando el dia o el mes se intruduzcan con un solo caracter

fecha = input("fecha: ")
partes = fecha.split("/")
valido = True
if len(partes[0]) == 2 and \
    len(partes[1]) == 2 and\
        len(partes[2] == 4):
            
    valido = True
    for p in partes: 
        if not p.isdigit():
            valido = False
            break
    
    if valido:
        print(f"dia: {partes[0]}, mes: {partes[1]}, año: {partes[2]}")
    else:
        print("formato no valido")
else:
    print("formato no valido")