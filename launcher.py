from colorama import *
from random import *
from os import *
import subprocess
import time

init(convert=True)

numberone = randint(1, 10)
numbertwo = randint(1, 10)

print(numberone, numbertwo)
print(Fore.LIGHTCYAN_EX + f"\n   Welcome to Snate's Snake!\n     To play you must answer this question! What is" + Fore.LIGHTGREEN_EX + f" {numberone} times {numbertwo}?")
correct = numberone * numbertwo
answer = input(Fore.LIGHTCYAN_EX + "\n       Put your answer here:")

try:
    answer = int(answer)
    if answer == correct:
        print(Fore.GREEN + "\n        Congrats! That's correct :)")
        input("\n         Press Enter to Continue...")
        subprocess.Popen(["python", "C:\\Users\\natea\\Desktop\\code\\pythonproject\\game1.py"],creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        print(Fore.LIGHTRED_EX + "\n        I'm sorry, that's not correct. The correct answer is", correct) 
        input("\n         Press Enter to Exit...")
except ValueError:
    print("Please enter a valid integer.")

