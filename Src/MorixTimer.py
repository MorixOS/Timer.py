import time 
import os
import platform

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

while True:
    clear_console()
    print("Welcome to MorixOS Timer!")
    timer = int(input("How long should the timer be (in seconds)?: "))
        
    while timer > 0:
        clear_console()
        print("Time left:", float(timer))
        timer -= 0.5
        time.sleep(0.5)
    
    clear_console()
    print("Time is up!")
     
    end = input("Do you want to set another timer? (yes/no): ")
    if end.lower() != "yes":
        clear_console()
        print("Exiting timer...")
        time.sleep(1)
        break