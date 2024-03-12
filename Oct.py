#a=int(input("Enter num:"))
#Lis=[]
#if a==0:
#    Lis.append(0)
#while a>=1:
#    Lis.append(a%2)
#    a=a//2
#print(Lis[::-1])
def todecimal(a):
    Lis=[]
    a2=a//8
    b=a2*8
    c=a-b
    i=0
    for i in range(i<=c):
        Lis.append(a2)
        Lis.append(c)
    print(Lis)
a=int(input("Enter num:"))
print(todecimal(a))
