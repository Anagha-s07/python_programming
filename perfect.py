num=int(input("Enter the number:"))
sum=0
for i in range(1,num):
 if(num % i==0):
  sum=sum+i
if(num==sum):
 print("The number is perfect")
else:
 print("The number is not perfect")
