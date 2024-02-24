import math
'''
a=int(input("Enter the of A: "))
b=int(input("Enter the of B: "))
c=int(input("Enter the of C: "))

d=(b*b)-(4*a*c)

if (d==0):
    x=-b/2*a
    print("Root of real & equal & are",x)

elif (d>0):
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b-math.sqrt(d))/2*a
    print("Root of real & unequal & are",x1,x2)

else:
    
    
    print("The Roots are imaginary")
'''


import math

a=float(input("Enter the of A: "))
b=float(input("Enter the of B: "))
c=float(input("Enter the of C: "))

d=(b*b)-(4*a*c)

if (d==0):
    x=-b/2*a
    print("Root of real & equal & are",x)

elif (d>0):
    x1=(-b+math.sqrt(d))/2*a
    x2=(-b-math.sqrt(d))/2*a
    print("Root of real & unequal & are",x1,x2)

else:
    
    
    print("The Roots are imaginary")







