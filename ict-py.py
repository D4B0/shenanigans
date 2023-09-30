import string
import random
import os

#Initialization
stopcode = ["0", "END", "CANCEL", "STOP"]
passcode = ""
def password_generate(len):
    # INIT
    available = string.printable
    password = ""
    max_len = len

    print(available)

    for i in range(len):
        password = password + random.choice(available)
    password = password.strip()
    print(password)
    return password




while True:
    print("Generate Password")
    pass_len = input("Length >> ")
    try:
        pass_len = int(pass_len)
        password_generate(pass_len)
        passcode = password_generate(pass_len)
        print(f"PASSCODE: {passcode}")
    except ValueError:
        if pass_len.lower() == "end".lower():
            print("Application Terminated")
            break
        elif pass_len.lower() == "show":
            pass
        else:
            print("Password Length must be number")

