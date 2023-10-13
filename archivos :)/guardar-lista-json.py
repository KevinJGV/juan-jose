import json
fd = open("archivos :)/lista.json", "w")

lst = [{"nombre":"paola", "edad": 25},
       {"nombre":"carlos", "edad": 28},
       {"nombre":"juan", "edad": 18},
       {"nombre":"mateo", "edad": 19},
       {"nombre":"patricia", "edad": 21},]

json.dump(lst, fd)

fd.close()