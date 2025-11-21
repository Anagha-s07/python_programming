def fibonacci(n):
	if n==0 or n==1:
		return n
	else:
		return fibonacci(n-1)+fibonacci(n-2)
n=int(input("Enter the number:"))
print("Fibonacci Series of",n,":")
for i in range(n):
	print("\t",fibonacci(i),end='')
print("\nThe ",n,"th fibonacci number is:",fibonacci(n-1))
