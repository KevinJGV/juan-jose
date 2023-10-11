Cadena = input("\nIngrese la cadena de caracteres: ")       
Longitud = len(Cadena)

Idx = 0                                                     # Variable para recorrer indices de la cadena
while True:
    #EVITAR ERROR DE INDEX
    if Idx <= (Longitud - 2):
        if Cadena[Idx] == Cadena[Idx+1]:                    # Si hay dos caracteres seguidos iguales -> Actualizo cadena
            #ACTUALIZAR CADENA
            Cadena = Cadena[:Idx] + Cadena[Idx+1:]          
            Cadena = Cadena[:Idx] + Cadena[Idx+1:]          # Reescribir cadena: Inicio hasta Idx + Idx+1 hasta Final
            Longitud = len(Cadena)                          # Actualizo Longitud de la nueva cadena
            Idx = 0                                         # Reinicio Indice para evaluar la nueva cadena desde 0
        else:                       
            Idx += 1                                        # Si no son iguales, evaluo el indice Siguiente                      
    else:
        #CONDICIONES DE SALIDA
        if Cadena == "":                                    
            print("Empty String")
        else:
            print(Cadena)
        break      