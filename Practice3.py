User = input("\t Enter user:")
pas = int(input("\t Enter pass:"))
Users = input("\t Enter user:")
pas1 = int(input("\t Enter pass:"))
if Users==User and pas1==pas:
    print("Welcom")
elif Users==User and pas1!=pas:
    print("Pass is wrong")
elif Users!=User and pas1==pas:
    print("User is wrong")
elif Users!=User and pas1!=pas:
    print("Both are wrong")









