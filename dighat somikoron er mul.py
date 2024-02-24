import math
a=int(input("Enter the valua of a :"))
b=int(input("Enter the valua of b :"))
c=int(input("Enter the valua of c :"))
d=b*b-4*a*c

if(d==0):
    x=-b/2*a
    print(x)
elif(d>0):
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b-math.sqrt(d))/2*a
    print(x1,x2)
else:
    print("The is imaginary")