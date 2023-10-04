new = int(input("English newspaper: "))
lstEng = []
for i in range(new):
    lstEng.append(input())

new = int(input("French newspaper: "))
lstFrench = []
for i in range(new):
    lstFrench.append(input())
    
result = set(lstEng) - set(lstFrench)
print("Student only English newspapers:", len(result))

#otra manera
n = int(input("English newspaper: "))
setEng = set()
for i in range(n):
    setEng.add(input())

n = int(input("French newspaper: "))
setFrench = set()
for i in range(n):
    setFrench.add(input())
    
result = setEng - setFrench
print("Student only English newspapers:", len(result))