n1 = 0
n2 = 1
n = 0
soma = 0

while n < 35:
	n = n1 + n2
	n1 = n2
	n2 = n
	if n%2 == 0:
		soma = soma + n

print soma