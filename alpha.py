n=int(input("Enter no of names:"))
names=[]
for i in range(1,n+1):
	#print("Enter name",i,":")
	name=input("Enter name:")
	names.append(name)
names.sort()
print("Names in alaphabetic order:")
for name in names:
	print(name)
