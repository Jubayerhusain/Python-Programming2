import math
a=int(input("Enter the valua of a:"))
b=int(input("Enter the valua of b:"))
c=int(input("Enter the valua of c:"))

if((a+b)>c and (b+c)>a and (c+a)>b):
    sum=(a+b+c)/2
    area=math.sqrt(sum*(sum-a)*(sum-b)*(sum-c))
    print("area of the triangle is",area)
else:
    print("the triangle is not possible")