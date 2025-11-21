n=int(input("Enter the number of elements:"))
a=[]
for i in range(n):
	element=input("Enter the element {}:".format(i+1))
	a.append(element)
max_length=a[0]
for element in a:
	if len(element)>len(max_length):
		max_length=element
print("word with longest length:",max_length)
print("length of longest word:",len(max_length))

