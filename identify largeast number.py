'''
num1=int(input("Enter the valua of Number 1: "))
num2=int(input("Enter the valua of Number 2: "))
num3=int(input("Enter the valua of Number 3: "))

if (num1 >= num2) and (num1 >= num3):
    largest=num1

elif (num2 >= num1) and (num2 >= num3):
    largest=num2

else:
    largest=num3

print("The largest Number among",largest )
'''
num1=float(input("Enter the valua of Number 1: "))
num2=float(input("Enter the valua of Number 2: "))
num3=float(input("Enter the valua of Number 3: "))

if (num1 >= num2) and (num1 >= num3):
    largest=num1

elif (num2 >= num1) and (num2 >= num3):
    largest=num2

else:
    largest=num3

print("The largest number", num1, ",", num2, "and", num3, "is=", largest)
