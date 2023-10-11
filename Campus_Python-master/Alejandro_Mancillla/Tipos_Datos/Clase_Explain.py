#TIPOS DE DATOS
numero1 = 10                        #E ntero
numero2 = 1.124568                  # Float
sNombre = "Oscar"                   # String
numero2 = "Daniel"                  # Dinamicas
sw = False

#OPERADORES ARITMETICOS
numero2 = numero1 // 2              # Division Entera (//)
numero2 = numero2 ** 2 * 3 - 2      # (), **, * /, + -
print(type(numero2))
print(numero2)

#OPERADOR DE CADENA
str1 = "Hola"
str2 = "Mundo"
str3 = str1 + " " + str2             # Concatenación (+)
print(str3)

str3 = str1 * 3                      # Repetición (*)
print(str3)

#FORMATEO DE CADENAS
print(f"Hola {str2}, {numero2}")                      # Cadena f-String = Imprime Texto mas contenido de la variable
print("Hola %s ,  %d" % ("Mundo", numero2))           # Cadenas con Formato = %Tipo de dato que viene a continuación
