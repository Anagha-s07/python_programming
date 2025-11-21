def sum_of_firstn(n):
	sum=0
	for i  in range(1,n+1):
		sum=sum+i
	return(sum)
n=int(input("Enter the number:"))
result=sum_of_firstn(n)
print("sum of ",n,"numbers:",result)
