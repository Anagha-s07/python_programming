def is_palindrome(n):
	n_str=str(n)
	n_rev=n_str[::-1]
	if n_str==n_rev :
		return(True)
	else:
		return(False)
n=int(input("Enter the number:"))
result=is_palindrome(n)
if result==True:
	print("THe number is a palindrome")
else:
	print("The number is not a palindrome")
	
