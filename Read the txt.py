import pyttsx3 
txt=pyttsx3.init()
while True:
    answer=input("What do you want him to say?")
    txt.say(answer)
    txt.runAndWait()
    c=input("Do you want to continue?(yes or no)" )
    if c=="no":
        break
    
