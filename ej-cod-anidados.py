# orden
print("el numero debe ser entre 0 y 10")
numero1 = int(input("ingrese un numero"))
numero2 = int(input("ingrese un numero"))
numero3 = int(input("ingrese un numero"))

if numero1 >= numero2 and numero1 >= numero3:
    if numero2 >= numero3:
        print(numero1, numero2, numero3)
    else:
        print(numero1, numero3, numero2)
      
elif numero2 >= numero3 and numero2 >= numero1:
    if numero1 >= numero3:
        print(numero2, numero1, numero3)
    else:
        print(numero2, numero3, numero1) 

    
elif numero3 >= numero2 and numero3 >= numero1:
    if numero2 >= numero1:
        print(numero3,numero2,numero1)
    else:
        print(numero3, numero1, numero2)
   
