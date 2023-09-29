señal = True
type1 = "door to door"
type2 = "telemarketing"
type3 = "sales executive"
totalVentas = 0
totalComisiones = 0

while señal == True:
    while True:
        try:
            cedula = input("Enter your ID: ")
            cedula = cedula.strip()
            cedula2 = cedula.replace(",","")
            cedula2 = cedula2.replace(".","")
            if len(cedula2) == 0 or cedula2.isdigit() == False or (len(cedula2) >= 8 and len(cedula2) <= 10) == False :
                if cedula == "-1":
                    bandera = False
                else:
                    print("Invalid ID format")
                    continue
            break
        except Exception as e:
                print(f"Error.Invalid ID.{e}")

    if señal == True:    
        while True:
            try:
                name = input("Enter seller name: ")
                name = name.strip()
                name2 = name.replace(" ","",3)
                if len(name2) == 0 or name2.isalnum() == False:
                    print("Invalid name format.")
                    continue
                break
            except Exception as e:
                print(f"Error.Invalid name.{e}")

        while True:
            try:
                contVentas = input("How much did you sell in the month:")
                contVentas = contVentas.strip()
                contVentas = float(contVentas.replace(",","."))
                if contVentas < 0 :
                    print("Invalid format, enter a positive number")
                    continue
                break
            except BaseException as e:
                print(f"Error.invalid format.{e}")

        while True:
            try:
                vendedor = int(input(f"Enter the type of seller, where:\n          [1]->{type1}\n          [2]->{type2}\n          [3]->{type3}\n ¿Que tipo de vendedor es?: "))
                if vendedor < 1 or vendedor > 3:
                    print("Number out of range")
                    continue
                break
            except Exception as e:
                print(f"Invalid format error.{e}")
    
        if vendedor == 1:
            comision = contVentas*(0.2)
            print(f"{name} identified with CC.{cedula} commission in the month: ${comision:,.0f} COP")
        elif vendedor == 2:
            comision = contVentas*(0.15)
            print(f"{name} identificado con CC.{cedula} commission in the month: ${comision:,.0f} COP")
        elif vendedor == 3:
            comision = contVentas*(0.25)
            print(f"{name} identificado con CC.{cedula} commission in the month: ${comision:,.0f} COP")
        totalVentas += contVentas
        totalComisiones += comision
print("\n")                   
print("="*10,"REPORTS OF THE MONTH","="*10)     
print(f"During the month, the following were sold: ${totalVentas:,.0f} COP")
print(f"During the month, employees commissioned : ${totalComisiones:,.0f} COP")