#LEER ARCHIVO JSON DE CUENTAS BANCARIAS Y GUARDAR EN OTRO ARCHIVO LAS CUENTAS CON SALDO MAYOR A 35.000.000

import json

with open("Ahorradores.json") as CuentasTotal:
    Data = json.load(CuentasTotal)

DataDian = []
Consecutivo = 1
for Cuenta in Data["cliente"]:
    if Cuenta["Saldo"] > 35000000:
        DataDian.append({
            "Consecutivo":Consecutivo,
            "NumCuenta":Cuenta["NumCuenta"],
            "Saldo":Cuenta["Saldo"]
        })
        Consecutivo += 1

with open("Dian.json","w")as Destino:
    json.dump(DataDian, Destino, indent = 4)