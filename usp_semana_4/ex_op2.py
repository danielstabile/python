n = int(input("Digite o valor de n: "))

c = 1
temp = n
adj = False
ultimo = -1

while c <= len(str(n)) and (not adj):
	resto = temp % 10
	temp = int(temp / 10)
	c = c+1
	if ultimo == resto:
		adj = True
		
	ultimo = resto
	
if adj:
	print("sim")
else:
	print("não")