def BuscarElement(List, Element):       #Función buscar en lista y devolver indice
    for i in range(len(List)):
        if List[i] == Element:
            return i
    return -1

def ExisteElement(List, Element):       #Funcion revisar si existe el elemento en Lista
    for e in List:
        if e == Element:
            return True
    return False

#LISTAS EXPLICACIÓN
MiLista = []                                                #Crear Lista Vacia
MiLista = list()                                            #Crear Lista Vacia0
print(MiLista)

#Metodos de Listas
MiLista.append("Alirio")                                    #Añadir elemento al final de la lista
print(MiLista)
print(MiLista, len(MiLista))                                #Len = Longitud de la lista
print(MiLista[0:1])                                         #Imprimir rango de Lista
MiLista.extend(["Andres", "Carlos", "Cristian", "Diana"])   #Añadir elementos al final de lista
print(MiLista, len(MiLista))
MiLista.pop()                                               #Elimina osición que se indique, Por defecto ultima posición
print(MiLista, len(MiLista))
MiLista.insert(2, "Lilian")                                 #Insertar objeto en posición indicada
print(MiLista, len(MiLista))
MiLista.remove("Carlos")                                    #Elimina el primer objeto que coincida con el ingresado
print(MiLista, len(MiLista))

print("=" * 20)
#Recorrer lista por indice
for idx in range(len(MiLista)):
    print(idx, "->", MiLista[idx])

print("=" * 20)
#Recorrer lista por elementos
for elem in MiLista:
    print(elem)

#Buscar elemento en Lista y devolver posición, sino devuelve -1
Pos = BuscarElement(MiLista, "Carlos")
print(Pos)
Pos = BuscarElement(MiLista, "Andres")
print(Pos)

#Buscar elemento en Lista, si esta, devuelve TRUE, sino FALSE
Esta = ExisteElement(MiLista, "Diana")
print(Esta)
Esta = ExisteElement(MiLista, "Andres")
print(Esta)

#Mas metodos de Listas
MiLista.count("Andres")         #Devuelve cantidad de veces que se encuentra un objeto indicado
MiLista.index("Lilian")         #Devuelve indice donde se encuentra el objeto indicado
MiLista.reverse()               #Invierte la lista
MiLista.sort()                  #Organiza la lista
MiLista.clear()                 #Limpia todos los elementos de la lista
