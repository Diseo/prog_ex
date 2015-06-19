def product():
	for num in reversed(range(100,1000)):
		for num2 in reversed(range(100,1000)):
			prod = num * num2
			if str(prod)[1] == str(prod)[4] and str(prod)[2] == str(prod)[3] and str(prod)[0] == str(prod)[-1:]:
				print num, num2, prod
				return

product()