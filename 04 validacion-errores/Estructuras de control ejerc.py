programa1 = "Técnico en sistemas"
programa2 = "Técnico en desarrollo de videojuegos"
programa3 = "Técnico en animación digital"
discount1 = "Beca por rendimiento"
discount2 = "Beca cultural"
discount3 = "SIN beca"
costoProgram1 = 800000
costoProgram2 = 1000000
costoProgram3 = 1200000
bandera = True
costMatriculas = 0

while bandera == True:
    codeNumber = input("\nIngrese el codigo del estudiante: ")
    name = input("Ingrese el nombre del estudiante: ")
    programStudent = int(input(f"Ingrese el programa al que perteneces, donde:\n             [1]->{programa1}\n             [2]->{programa2}\n             [3]->{programa3}:\nEl programa es= "))
    discount = int(input(f"Digite del 1 al 3 dependiendo del estudiante, donde:\n             [1]->{discount1}\n             [2]->{discount2}\n             [3]->{discount3}:\nEl programa es= "))
    if programStudent == 1:
        if discount == 1:
            cost2pay = costoProgram1/2
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es {cost2pay:,.0f}COP")
        elif discount == 2:
            cost2pay = costoProgram1*(1-0.4)
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es {cost2pay:,.0f}COP")
        else:
            cost2pay = costoProgram1
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es: ${cost2pay:,.0f}COP")
    if programStudent == 2:
        if discount == 1:
            cost2pay = costoProgram2
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es: ${cost2pay:,.0f}COP")
        elif discount == 2:
            cost2pay = costoProgram2*(1-0.4)
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es: ${cost2pay:,.0f}COP")
        elif discount == 3:
            cost2pay = costoProgram2
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es: ${cost2pay:,.0f}COP")
    if programStudent == 3:
        if discount == 1:
            cost2pay = costoProgram3/2
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es: ${cost2pay:,.0f}COP")
        elif discount == 2:
            cost2pay = costoProgram3*(1-0.4)
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es: ${cost2pay:,.0f}COP")
        elif discount == 3:
            cost2pay = costoProgram3
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es: ${cost2pay:,.0f}COP")
    bandera2 = input("¿Desea continuar? ")
    if bandera2 == "SI" or bandera2 == "si":
            bandera = True
    else:
            bandera = False