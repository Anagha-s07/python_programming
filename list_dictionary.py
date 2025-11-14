std={}
n=int(input("Enter the no of students:"))
for i in range(n):
	name=input("Enter student name:")
	age=int(input("Enter the age:"))
	grade=input("Enter the grade:")
	std[name]=(age,grade)
print("\nStudent records:")
for name,details in std.items():
	print("Name:",name,"|Age:",details[0],"|Grade:",details[1])
