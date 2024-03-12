while True:
    n=int(input("N:"))
    i=2
    if n>1:
        while i<n:
            if n%i==0:
                print("Its not prime")
                break
            i+=1
        else:
            print("Its prime")
    else:
     print("Its not prime")
    
