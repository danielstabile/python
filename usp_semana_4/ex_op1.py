n = int(input("Digite o valor de n: "))

c = 1
primo = True

if n <=2:
	primo = False

while c < n-1 and primo:
	resto = n % (n - c)
	c = c+1
	if resto == 0:
		primo = False

if primo:
	print("primo")
else:
	print("não primo")