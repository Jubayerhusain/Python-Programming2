
import math

p=int(input("Enter The valua of P: "))
q=int(input("Enter The valua of Q: "))
r=int(input("Enter The valua of R: "))

d=(q*q)-(4*p*r)

if d==0:
    a= -q/2*p
    print(a)
    
elif d>0:
    a1=(-q+math.sprt(d))/2*p
    a2=(-q-math.sprt(d))/2*p
    
    print(int(a1),int(a2))
    
else:
    print("triangle is not possible")






