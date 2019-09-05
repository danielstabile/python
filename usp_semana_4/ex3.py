n = int(input("Digite o valor de n: "))

temp = n
c = 1
soma = 0

while c <= len(str(n)):
	resto = temp%10
	temp = int(temp/10)
	soma = soma + resto
	c = c+1
	
print(soma)