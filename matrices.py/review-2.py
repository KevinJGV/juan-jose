def main():

    redFerrocarriles = {}

    N = int(input("Número de ciudades: "))

    for i in range(N):
        nombreCiudad = input(f"Nombre de la ciudad {i + 1}: ")
        conexiones = input(f"Ciudades enlazadas a {nombreCiudad}: ").split(',')
        redFerrocarriles[nombreCiudad] = conexiones


    ciudadOrigen = input("Ciudad de salida: ")
    ciudadDestino = input("Ciudad de destino: ")


    if hayViaDirecta(redFerrocarriles, ciudadOrigen, ciudadDestino):
        print("Hay una vía directa entre las ciudades.")
    else:
        print("No hay una vía directa entre las ciudades.")

def hayViaDirecta(redFerrocarriles, ciudadOrigen, ciudadDestino):
    visitados = set()
    via = [ciudadOrigen]

    while via:
        ciudadActual = via.pop(0)
        if ciudadActual == ciudadDestino:
            return True

        visitados.add(ciudadActual)

        for ciudadVecina in redFerrocarriles.get(ciudadActual, []):
            if ciudadVecina not in visitados:
                via.append(ciudadVecina)

    return False

if __name__ == "__main__":
    main()
    