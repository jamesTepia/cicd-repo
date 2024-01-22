# test_vulnerability.py

import os

def insecure_function(user_input):
    command = "echo " + user_input
    os.system(command)

if __name__ == "__main__":
    user_input = input("Enter something to echo: ")
    insecure_function(user_input)