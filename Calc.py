import pyttsx3
import os
r=pyttsx3.init()
r.say("Welcom to Dani and Arya calculator")
r.runAndWait()
while True:
    r.say("Chose your operator:")
    r.runAndWait()
    oper=int(input("\t Chose your operator:\n\t1)+\t2)-\t3)*\t4)/\t5)%\t6)avg\t7)Exit\n"))
    if oper==7:
        r.say("Good bye!")
        r.runAndWait()
        break
    r.say("Enter number1 and number2:")
    r.runAndWait()
    num1 , num2=float(input("\tEnter num1:")),float(input("\tEnter num2:"))
    if oper==1:
        c=num1+num2
        print(f"\t{num1}+{num2}={c}")
        r.say(c)
        r.runAndWait()
    if oper==2:
        c=num1-num2
        print(f"\t{num1}-{num2}={c}")
        r.say(c)
        r.runAndWait()
    if oper==3:
        c=num1*num2
        print(f"\t{num1}*{num2}={c}")
        r.say(c)
        r.runAndWait()
    if oper==4:
        if num2==0:
            r.say("You cannot divide a number by zero. Please try again")
            r.runAndWait()
            continue
        c=num1/num2
        print(f"\t{num1}/{num2}={c}")
        r.say(c)
        r.runAndWait()
    if oper==5:
        if num2==0:
            r.say("You cannot divide a number by zero. Please try again")
            r.runAndWait()
            continue
        c=num1%num2
        print(f"\t{num1}%{num2}={c}")
        r.say(c)
        r.runAndWait()
    if oper==6:
        c=(num1+num2)/2
        print(f"\t({num1}+{num2})/2={c}")
        r.say(c)
        r.runAndWait()