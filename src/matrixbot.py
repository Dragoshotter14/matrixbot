import string
import random
import time
from selenium import webdriver
from operator import truediv
import keyboard 


print("##############################")
print("### Welcome to Matrix Bot  ###")
print("##############################")
while True:
    print("Welcome to the menu, if you type 1 you will be redirected to a completely manual form \n" )
    option = input("Option:")
    if option == "1":
        nameAccount = input("Enter a unique name for your accounts:")
        break
    elif option == "2":
        accountNumber = int(input("Type 1 if you want to create 'infinite accounts' and type 2 if you want to create only 1 \n"))
        def randomAccount(chars = string.ascii_lowercase + string.digits, N=10):
            return "".join(random.choice(chars) for _ in range(N))
        def randomPassword(chars = string.ascii_lowercase + string.digits, N=14):
            return "".join(random.choice(chars) for _ in range(N))
        if accountNumber == 1:
            while True:
                print("This is your automatically generated account: \n", randomAccount(N=10))
                time.sleep(0)
                print("This is your automatically generated password: \n", randomPassword(N=10))
                time.sleep(5)
                AreYouStillHere = input("Press Enter if you have created enough accounts \n")
        if accountNumber == 2:
            print("This is your automatically generated account: \n", randomAccount(N=10))
            print("This is your automatically generated password: \n", randomPassword(N=10))
            


    

