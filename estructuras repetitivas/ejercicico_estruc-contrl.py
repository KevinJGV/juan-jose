n = int(input("cuantos usuarios?"))

for i in range(1, n + 1):
    print(f"\nDatos del usuario #{i}")
    cod = input("codigo? ")
    nom = input("nombre? ")
    est = input("estado [V: vigente o S: suspendido]? ")
    estr = (input("Estrato [1 al 6]? "))
    con = float(input("Consumo de agua al mes [cm3]? "))
    
    if est == "v" or est == "V":
        if estr == 1:
            tbas = 10000
        elif estr == 2:
            tbas = 20000
        elif estr == 3:
            tbas = 30000
        elif estr == 4:
            tbas = 45000
        elif estr == 5:
            tbas = 60000
        elif estr == 6:
            tbas = 70000
        else:
            tbas = 0
            
        valcons = con * 200
          
        valpagar = tbas + valcons
        
        print("\n", "=" * 40)
        print("\tNombre: ", nom)
        print(f"\tValor traifa basica: ${tbas:,}")
        print(f"\ttValor consumo: ${valcons:,.0f}")
        print(f"\tValor de la factura de agua: ${valpagar:,.0f}")