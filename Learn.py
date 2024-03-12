a=int(input("Enter num:"))
b=0
for i in range(1,a):
    if a%i==0:
        b+=i
if b==a:
    print("Compelete")
else:
    print("Is not compelete")