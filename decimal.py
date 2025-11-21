d=int(input("Enter the decimal:"))

b=""
if d==0:
	b="0"
else:
	n=d
	while n>0:
		b=str(n%2)+b
		n=n//2
print("Binary equivalent:",b)

	

