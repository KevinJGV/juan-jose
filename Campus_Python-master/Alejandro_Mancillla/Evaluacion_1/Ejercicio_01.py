#FACTURA DE COMPRA
print("FACTURA DE COMPRA\n")

#DATOS DE ENTRADA
Precio = float(input("Ingrese el precio del Articulo: "))
Unidades = int(input("Indique cantidad de unidades a comprar: "))

Descuento = 0
Iva = 0

#PROCESO
PreNeto = Precio * Unidades
Iva = PreNeto * 0.15
PreBruto = PreNeto + Iva
if PreBruto > 1000:
    Descuento = PreBruto *0.05
ValorTotal = PreBruto - Descuento

#SALIDA
print("\n","-" * 30)
print("FACTURA DE COMPRA")
print("\t","-" * 30)
print(f"\tValor Articulo = {Precio}")
print(f"\tUnidades = {Unidades}")
print(f"\tPrecio Neto = {PreNeto}")
print(f"\tIVA = {Iva}")
print(f"\tDescuento = {Descuento}")
print("\t","-" * 30)
print(f"\tValor a Pagar = {ValorTotal}")
print("\t","-" * 30)