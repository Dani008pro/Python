import datetime 
import os
import time
while True:
    a=datetime.datetime.now()
    print(f"H={a.hour} : M={a.minute} : S={a.second}")
    time.sleep(1)
    os.system("cls")

