def add(x,y):
	return x+y
def sub(x,y):
	return x-y
def multiply(x,y):
	return x*y
def divide(x,y):
	return x/y
def power(x,y):
	return x**y
def mod(x,y):
	return x%y
def calculator(x,y,operator):
	if operator =="+" :
		return add(x,y)
	elif operator =="-":
		return sub(x,y)
	elif operator =="-":
		return sub(x,y)
	elif operator =="*":
		return multiply(x,y)
	elif operator =="/":
		return divide(x,y)
	elif operator =="**":
		return power(x,y)
	elif operator =="%":
		return mod(x,y)	
	else:
		print("Invalid")
x=float(input("Enter the first number:"))
y=float(input("Enter the second number:"))
operator=input("Enter the operator:")
result=calculator(x,y,operator)
print("Result:",result)	
