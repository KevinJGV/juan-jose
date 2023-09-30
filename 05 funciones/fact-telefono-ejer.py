def calcularValorImpulso(impulso):
    return 100 * impulso

def calcularTarifaBasica(estrato):  
    if estrato == 1:
        return 10000
    elif estrato == 2:
        return 15000
    elif estrato == 3:
        return 20000
    elif estrato == 4:
        return 25000
    else:
        return 30000    
    
    
def leerestrato(msj):
    while True:
        try:
            n = int(input(msj))
            if n < 1 or n > 5:
                print("Estrato invalido. ingrese el estrato del usuario: ")
                continue
                return n 
        except ValueError:
            print("Error al ingresar el estrato.")
            
def leernombre(msj):
    while True:
        try:
            nom = str(input(msj))
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre invalido")
                continue
                return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)
            
def leerint(msj):
    while True: 
        try:
            n = int(input(msj))
            if n < 1:
                print("Valor invalido. Debe ser mayor a cero")
                continue
                return n 
        except ValueError:
            print("Error al ingresar el nombre.")
    
n = leerint("Ingrese la cantidad de usuarios: ")
valtot = 0
for i in range(1, n+1):
    print("\nDatos del usuario #", i)
    nombre = leernombre("nombre?: ")
    estrato = leerestrato("Estrato? ") 
    impulso = leerint("impulsos?")
    valtbas = calcularTarifaBasica(estrato)
    valimpu = calcularValorImpulso(impulso)
    
    print("=" * 30)
    print("nombre", nombre)
    print("Tarifa basica", valtbas)
    print("Valor de impulsos:", valimpu)
    
    valtot += valtbas + valimpu

print("\n", "*" * 30)
print("El valor toatal a pagar es: ", valtot)