while(1):
    import math
    a=int(input("Enter the value of a :"))
    b=int(input("Enter the value of b :"))
    c=int(input("Enter the value of c :"))

    d=b*b-4*a*c

    if d==0:
        x=-b/2*a
        print(x)
    elif d>0:
        x1=(-b+math.sqrt(d))/2*a
        x2=(-b-math.sqrt(d))/2*a
        print (x1,x2)
    else :
        print("triangle is not possible (-_-)")