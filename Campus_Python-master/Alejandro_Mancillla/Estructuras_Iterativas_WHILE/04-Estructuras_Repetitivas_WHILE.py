Valida = False

while Valida == False:
    Contra = input("Ingrese una contraseña: ")
    Longitud = len(Contra)
    MayMin = Contra.swapcase()
    Numeros = 0
    Espacios = 0
    Especiales = 0
 
    #CONDICIÓN DE LONGITUD
    if(Longitud >= 8):
        #CONDICIÓN MINUS Y MAYUS
        if MayMin != Contra.upper() and MayMin != Contra.lower():
            for i in range(1, Longitud):
                #CONDICION NUMEROS
                if Contra[i].isdigit() == True:
                    Numeros += 1
                #CONDICION ESPACIOS
                if Contra[i] == " ":
                    Espacios += 1
                #CONDICIÓN CARACTERES ESPECIALES
                if Contra[i] == "%" or Contra[i] == "&" or Contra[i] == "^":
                    Especiales += 1
            if Numeros > 0:
                if Espacios == 0:
                    if Especiales > 0:
                        Valida = True
                    else:
                        print("\nCONTRASEÑA INVALIDA")
                        print("No contiene caracter especial")
                else:
                    print("\nCONTRASEÑA INVALIDA")
                    print("Tiene Espacios")
            else:
                print("\nCONTRASEÑA INVALIDA")
                print("NO Tiene Numeros")         
        else:
            print("CONTRASEÑA INVALIDA")
            print("La contraseña no tiene al menos 1 Minuscula y 1 Mayuscula")
    else:
        print("CONTRASEÑA INVALIDA")
        print("La contraseña tiene menos de 8 digitos")

if Valida == True:
    print("\nCONTRASEÑA VALIDA")
    print("Cumple con todas las condiciones")