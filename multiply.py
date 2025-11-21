n=int(input("Enter the number for which multiplication table to be generate="))
end=int(input("Enter the end value="))
for i in range(1,end+1):
 mul=i*n
 print(i,"*",n,"=",mul)
