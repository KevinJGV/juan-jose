def findElemListPos(lst, elem):
    #funcion que busca un elemento en la lista, si lo encuentra devuelve p
    #si no lo encuentra devuelve -1
    for p in range(len(lst)):
        if elem == lst[p]:
            return p
    return -1

def findElemList(lst, elem):
    #funcion que busca un elemento en la lista
    #si lo encuentra devuelve true
    # si no lo encuentra devuelve false
    
    for e in lst:
        if e == elem:
            return True
        return False