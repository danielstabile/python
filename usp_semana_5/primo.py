def is_primo(n):
	primo = True
	resto = 1
	i = n
	while i - 1 > 1 and resto != 0:
		i = i - 1		
		resto = n % i
		if resto != 0:
			primo = True
		else:
			primo = False
	return primo

def maior_primo(n):
	ret = 0
	if n >= 2:
		while n >= 2 and ret == 0:
			temp = is_primo(n)
			if temp:
				ret = n
			else:
				n = n - 1
	return ret

x = int(input("num: "))
ret = maior_primo(x)

print(ret)