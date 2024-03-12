#a=int(input("enter num:"))
#
# data=[]
#for i in range(1,a):
#    b=int(input("Enter b:"))
#   data.append(b)
#newdata=list(set(data))
#file=open("D:/Dani.txt","w")
#for c in newdata:
#    file.write(str(c)+'\n')
#file.close()
x='12,14,16,18,20'
y=x.split(',')
b=[]
for i in y:
    b.append(int(i))
print(sum(b))