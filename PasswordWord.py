def alaki(a:str):
    newstr=""
    for i in a:
        x=ord(i)*10
        newstr+=chr(x)
    return newstr
def real(a:str):
    newstr=""
    for i in a:
        x=ord(i)//10
        newstr+=chr(x)
    return newstr
u=int(input("How many?"))
for _ in range(1,u+1):
    a=input("Enter word:")
    b=alaki(a)
    print(b)
    g=int(input("Enter pass:"))
    if g==1234:
        print(a)
    else:
        print("Really?\tGo out!")
        break
    
    

