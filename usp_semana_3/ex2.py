#Exercicio 3: Escreva um programa que resolva uma equação de segundo grau.   
#ax² + bx + c = 0
# x = – b ± √delta / 2	* a
# delta = b² – 4 * a * c

import math

coef_a = int(input("Digite o coeficiente A: "))
coef_b = int(input("Digite o coeficiente B: "))
coef_c = int(input("Digite o coeficiente C: "))
x1 = 0
x2 = 1
msg = ""

delta = math.pow(coef_b,2) - (4 * coef_a * coef_c)

if delta >= 0:
	x1 = (-1 * (coef_b) + (math.sqrt(delta))) / (2 * coef_a)
	x2 = (-1 * (coef_b) - (math.sqrt(delta))) / (2 * coef_a)
	if x1 < x2:
		msg = "as raízes da equação são " + str(x1) + " e " + str(x2)
	else:
		msg = "as raízes da equação são " + str(x2) + " e " + str(x1)
else:
	msg = "esta equação não possui raízes reais"

if x1 == x2:
	msg = "a raiz desta equação é " + str(x1)

#print(delta)
print(msg)