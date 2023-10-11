#Este programa recibe la matriz de ventas semanales de la empresa SweetCo

def calcDiaMaxIngresos(matVtas, matPrecios):
    fils = len(matVtas)
    cols = len(matVtas[0])
    lstVtasDia = [0] * cols
    for f in range(fils):
        for c in range(cols):
            lstVtasDia[c] += matVtas[f][c] * matPrecios[f]
            
    print(lstVtasDia)
    diaMaxVtas = max(lstVtasDia)
    posDia = lstVtasDia.index(diaMaxVtas)
    return posDia

def calcProdMaxIngresosSem(matVtas, matPrecios):
    fil = len(matVtas)
    lstTotVtas = [0] * fil
    for f in range(fil):
        lstTotVtas[f] = sum(matVtas[f]) * matPrecios[f]

#print(lstTotVtas)
    maxVtas = max(lstTotVtas)
    prodMaxVtas = lstTotVtas.index(maxVtas) + 1
    return prodMaxVtas


matPrecios = [1500, 5000, 6500, 2500, 22500 ]
matVtas = [[100, 88, 92, 94, 85, 110, 118],
             [30, 42, 31, 32, 38, 40, 37],
             [23, 35, 39, 45, 55, 60, 61],
             [45, 50, 56, 65, 47, 57, 68],
             [18, 25, 33, 21, 22, 28, 32]]

prodMaxIngSem = calcProdMaxIngresosSem(matVtas, matPrecios)
print("El producto que mas genera ingresos en al semana es: ", prodMaxIngSem)

dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
diaMaxIngreso = calcDiaMaxIngresos(matVtas, matPrecios)
print("el dia que genera ingresos en es:", dias[diaMaxIngreso])


#el de manuel medrano

def calcProdMasIngSem(matVentas, matPrecios):
    fil = len(matVentas)
    lstTotalVentas = [0] * fil
    for f in range(fil):
        lstTotalVentas[f] = sum(matVentas[f] * matPrecios[f])
    maxventas = max(lstTotalVentas)
    prodMaxVentas = lstTotalVentas.index(maxventas)  + 1
    return prodMaxVentas


def calcDiaMasIngSem(matVentas, matPrecios):
    lstTotalVentas = [0] * 7
    for f in range(len(matVentas)):
        for c in range(len(matVentas[f])):
            lstTotalVentas[c] = lstTotalVentas[c] + (matVentas[f][c] * matPrecios[f])



    maxVentas = max(lstTotalVentas)
    diaMaxVentas = lstTotalVentas.index(maxVentas) + 1
    return diaMaxVentas


matPrecios = [1500,5000,6500,2500,22500]
matVentas = [[100,88,92,94,85,110,118],
                [30,42,31,32,38,40,37],
                [23,35,39,45,55,60,61],
                [45,50,56,65,47,57,68],
                [18,25,33,21,22,28,32]]


prodMasIngSem = calcProdMasIngSem(matVentas, matPrecios)
print(f"El producto de mas ingreso es el: {prodMasIngSem}")

diaMasIngSem = calcDiaMasIngSem(matVentas, matPrecios)
if diaMasIngSem == 7:
    print(f"El dia de mas ingreso es el:{diaMasIngSem} o domingo...")














