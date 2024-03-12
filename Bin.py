def Decimal_to_binery(a):
    Lis=[]
    if a==0:
        Lis.append(0)
    while a>=1:
        Lis.append(a%2)
        a=a//2
    print(Lis[::-1])
a=int(input("Enter num:"))
print(Decimal_to_binery(a))
