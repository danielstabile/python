#5 Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.

n1 = int(input("Informe o primeiro numero: "))
n2 = int(input("Informe o segundo numero: "))
sinal = input("Informe o segundo numero: ")
resultado = 0
sinal_ok = 1

if sinal == "+":
	resultado = n1 + n2
elif sinal == "-":
	resultado = n1 - n2
elif sinal == "*":
	resultado = n1 * n2
elif sinal == "/":
	resultado = n1 / n2
else:
	print("Operador invalido")
	sinal_ok = 0

if sinal_ok > 0:
	print(str(resultado))
