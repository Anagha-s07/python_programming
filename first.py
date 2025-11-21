string=input("Enter a string:")
start=string[-1]
end=string[0]
if len(string)>1 :
       new_str=start+string[1:-1]+end
else:
       new_str=string
print("new String:",new_str)
