print("CALCULADORA NOMINA EMPLEADO\n")

#INGRESO DE DATOS
HorasTrabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
ValorHora = 20000

#PROCESO
SueldoBruto = HorasTrabajadas * ValorHora
DescuentoEPS = SueldoBruto * 0.04
DescuentoPension = SueldoBruto * 0.04
SueldoNeto = SueldoBruto - DescuentoEPS - DescuentoPension

#SALIDA
print(f"SUELDO BRUTO = {SueldoBruto} \n -DESCUENTO EPS = {DescuentoEPS} \n -DESCUENTO PENSION = {DescuentoPension} \nSUELDO NETO = {SueldoNeto}")