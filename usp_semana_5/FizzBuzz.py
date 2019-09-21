def fizzbuzz(n):
	resto3 = n % 3
	resto5 = n % 5
	ret = ""

	if resto3 == 0 and resto5 != 0:
		ret = "Fizz"
	elif resto3 != 0 and resto5 == 0:
		ret = "Buzz"
	elif resto3 == 0 and resto5 == 0:
		ret = "FizzBuzz"
	else:
		ret = n
	return ret

# x = fizzbuzz(int(input("numero: ")))
# print(x)