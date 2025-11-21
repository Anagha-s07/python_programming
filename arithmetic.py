a=int(input("ENTER FIRST NUMBER:"))
b=int(input("ENTER SECOND NUMBER:"))
c=input("ENTER THE OPERATOR:")
if c ==  '+' :
   print("SUM=",a+b)
elif c ==  '-' :
    print("DIFFERENCE=",a-b)
elif c ==  '*' :
    print("PRODUCT=",a*b)
elif c ==  '/' :
    print("DIVISION=",a/b)
elif c ==  '**' :
    print("POWER=",a**b)
elif c ==  '%' :
    print("MOD=",a%b)
elif c ==  '//' :
    print("FLOOR=",a//b)  
else:
    print("INVALID ")  
