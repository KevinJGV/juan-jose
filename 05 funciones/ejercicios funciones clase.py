
"""def distacia(xt, yt, xs, ys):
    d = math.sqrt((xt - xs)** 2 + (yt - ys)** 2)
    return d
x1 = 1
x2 = 2
y1 = 3
y2 = 4
dist = distacia(x1, y1, x2, y2)
print(f"la distancia es {dist:.3f}") """

#2
"""import math
def distacia(xt, yt, xs, ys):
    d = math.sqrt((xt - xs)** 2 + (yt - ys)** 2)
    return d

def perimetro_triangulo(xp, yp, xr, yr, xq, yq):
    perimetro = distacia(xp, yp, xr, yr) + distacia(xr, yr, xq, yq) + distacia(xp, yp, xq, yq)
    return perimetro

x1 = 1
y1 = 4
x2 = 3
y2 = 0
x3 = 5
y3 = 3

print(f"el perimetro del triangulo es {perimetro_triangulo(x1, y1, x2, y2, x3, y3):.3f}")"""
# 3 # la def no calcula
"""def descuento(valArticulo):
    
    if valArticulo > 150000:
        descuento = valArticulo * 0.05
    else:
        descuento = 0
    return descuento
        
        
valArticulo = int(input("ingrese el valor del articulo: "))
print(f"el descuento de su articulo es de {descuento(valArticulo):.0f}")"""
#4
"""def notas(n1,n2,n3,n4,n5):
    prom = (n1+n2+n3+n4+n5) / 5
    if prom > 3.5:
        return True
    else:
        return False

    
nota1 = float(input("ingrese la nota 1: "))
nota2 = float(input("ingrese la nota 2: "))
nota3 = float(input("ingrese la nota 3: "))
nota4 = float(input("ingrese la nota 4: "))
nota5 = float(input("ingrese la nota 5: "))

if notas(nota1,nota2,nota3,nota4,nota5):
    print("ganó el año")
else:
    print("Perdió el año")"""
    
#5
import turtle
#draw a line from (x1, y1) to (x2, y2)
def drawLine(x1, y1, x2, y2):
    turtle.penup()

    turtle.goto(x1, y1)
    turtle.pendown()
    turtle.goto(x2, y2)
    
#write a string s at the specified location (x, y)
def writetext(s, x,y):
    turtle.penup() # pull the pen up
    turtle.goto(x,y)
    turtle.pendown() # pull the pen down
    turtle.write(s) # write a string
    
# draw a point at the specified location (x,y)
def drawPoint(x, y):
    turtle.penup() #pull the pen up
    turtle.goto(x, y)
    turtle.pendown() #pullthe pen down
    turtle.begin_fill() #begin to fill colo in a shape
    turtle.circle(3)
    turtle.end_fill() #fill the shape
    
#draw a circle centered at (x, y) with the specified radius
def drawCircle(x = 0, y = 0, radius = 10):
    turtle.penup()
    turtle.goto(x, y - radius)
    turtle.pendown
    turtle.circle(radius)

#draw a rectangle at (x, y) with the specified width and height
def drawRectangle(x = 0, y = 0, width = 10, height = 10):
    turtle.penup()
    turtle.goto(x = 0 + width / 2, y + height )
    
    