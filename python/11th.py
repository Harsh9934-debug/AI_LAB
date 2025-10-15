def fibo(n):
	a, b = 0, 1
	result = []
	for _ in range(n):
		result.append(a)
		a, b = b, a + b
	return result

terms = int(input("enter the number of terms: "))
fibosq = fibo(terms)
print(fibosq)
