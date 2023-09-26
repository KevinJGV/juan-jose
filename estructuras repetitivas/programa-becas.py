#ejercicio
tecnico_en_sistemas = 800000
tecnico_en_desarrollo_de_videojuegos = 1000000
tecnico_en_animacion_digital = 1200000
n = int(input("ingrese su codigo de su instituto "))
for i in range(1):
    print(f"\nDatos del usuario ")
    cod = input("codigo? ")
    nom = input("nombre? ")
    print("programa cacademico al que pertenece?")
    programa = input("tecnico en sistemas", "tecnico en desarrollo de videojuegos", "tecnico en animacion digital")
    if programa == tecnico_en_sistemas: