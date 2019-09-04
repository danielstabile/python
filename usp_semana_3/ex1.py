import math

x1 = float(input("Digite a cordenada x1 do plano cartesiano: "))
y1 = float(input("Digite a cordenada y1 do plano cartesiano: "))
x2 = float(input("Digite a cordenada X2 do plano cartesiano: "))
y2 = float(input("Digite a cordenada y2 do plano cartesiano: "))

#d(x,y)= raiz(x1-x2)^2 + (y1-y2)^2

d1 = (x1-x2) **2
d2 = (y1-y2) **2
distancia = math.sqrt(d1+d2)

if distancia >=10:
	print("longe")
else:
    print("perto")
