def vogal(vog):
	ret = False
	if (vog == "a" or vog == "e" or vog == "i" or vog == "o" or vog == "u" or vog == "A" or vog == "E" or vog == "I" or vog == "O" or vog == "U"):
		ret = True
	else:
		ret = False
	return ret

# x = vogal(input("letra: "))
# if x:
# 	print("vogal")
# else:
# 	print("consoante")