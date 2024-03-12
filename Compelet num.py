n=int(input("Enter num: \t"))
L=0
for i in range(1,n,1):
    if n%i==0:
        L+=i
if L==n:
    print("Compelete")
else:
    print("No")


