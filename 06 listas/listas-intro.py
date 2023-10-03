milista = [] #lista vacia
milista = list() #lista vacia
nomCampers = ["Juan", "Yulieth", "Lorenzo" , "Manuel", "David"]
print(nomCampers)
print(nomCampers[1])
nomCampers[1] = "julieth"
print(nomCampers[5])

#slices
print(nomCampers[2:4])
print(nomCampers[::-1]) #recorre de atras a adelante

nomCampers_juan =  ["Daniela", "Maria", "Juliana", "Sandra", "Calorina"]
print( nomCampers_juan)
# nomCampers += nomCampers_juan
# print(nomCampers)

#METODOS DE LISTAS
nomCampers.append("Kevin") #lista entre lista sirve append
print(nomCampers)

nomCampers.extend(nomCampers_juan)     #no para agregar vomo lista
print(nomCampers)
print(nomCampers[-1])

# insert
nomCampers.insert("Carlos")
print(nomCampers)

nomCampers.pop() #elimina ultimo elemento
print(nomCampers)
nomCampers.pop(-3)
print(nomCampers)

#remove

nomCampers.remove("Sandra")
print(nomCampers)

#sort

nomCampers.sort()
print(nomCampers)

nomCampers.insert(2, "Daniel")
nomCampers.sort()
print(nomCampers)

# list2 = [0, 1, 15, "115"]
# list2.sort()
# print(list2)

nomCampers.sort(reverse=True)
print(nomCampers)





