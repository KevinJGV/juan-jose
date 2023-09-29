#la definicion de la funcion}
def long_string(str):
    try:
        long = 0
        while str[long] != None:
            long += 1
    except:
        pass
    return long

def preparar_cafe(insumo1, insumo2):
    if insumo1.lower() == "cafe" and insumo2.lower() == "agua":
        salida  = "tinto"
    else:
        salida = "daño la caferera"
    return salida

#uso de la función 

vaso = preparar_cafe("cafe", "agua")
print(vaso)

print (long_string(vaso))