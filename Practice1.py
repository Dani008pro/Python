import math
print("Enter a,b,c:")
a=float(input())
b=float(input())
c=float(input())
delta=b*b-4*a*c
if delta>0:
    x1=-b+math.sqrt(delta)/(2*a)
    x2=-b-math.sqrt(delta)/(2*a)
    print(f"x1={x1} x2={x2}")
elif delta<0:
    print("Not a root")
elif delta==0:
    x1=-b/(2*a)
    print(f"x1={x1}  x2={x1} \n x1=x2")
