#ENCONTRAR PALABRA CLAVE
Clave= input("INGRESE UNA PALABRA CLAVE:")
Clave = Clave.lower()
Oracion = ""
Buscar = -1

while Buscar == -1:
    Oracion = input("Ingrese la Oración: \n")
    Oracion = Oracion.lower()
    Buscar = Oracion.find(Clave)
    if Oracion == "salir":
        break
    if Buscar < 0:
        print("La palabra no se encuentra en la oración\n\nINGRESE OTRA ORACIÓN")
    else:
        break

if Buscar >= 0:
    print("LA PALABRA CLAVE SÍ ESTÁ EN LA ORACIÓN")