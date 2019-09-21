def maximo(n1, n2, n3):
	ret = 0
	if n1 >= n2 and n1 >= n3:
		ret = n1
	elif n2 > n1 and n2 > n3:
		ret = n2
	else:
		ret = n3
	return ret

x1 = input("num 1: ")
x2 = input("num 2: ")
x3 = input("num 3: ")

print(maximo(x1, x2, x3))