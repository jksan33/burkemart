# -*- coding: utf-8 -*-
"""
@author: WyldPhyr
"""

from random import randint

num = randint(0,9)

def run():
#   This is to prevent the rest of the program from running until the user asks
#   a question. Plus there's a super secret Easter egg!
    question = raw_input("What is your yes or no question? ")

#   Easter egg (super secret)
    if question in ["password123"]:
        print("Happy Easter!")
    else:
        print(" ")
    
    if num == 0:
        print("Yes, and you will be happy!")
    elif num == 1:
        print("No, and if you try, it will not end well.")
    elif num == 2:
        print("Yes.")
    elif num == 3:
        print("No.")
    elif num == 4:
        print("Maybe so.")
    elif num == 5:
        print("Perhaps.")
    elif num == 6:
        print("Without a doubt.")
    elif num == 7:
        print("Only on Sundays.")
    elif num == 8:
        print("Ask again later.")
    elif num == 9:
        print("42.")
    else:
#       Yay for error messages!
        print("Sorry, the future is cloudy today. Please restart and try again.")
        rep()

def rep():
    repeat = raw_input("Would you like to ask another question? ")
    if repeat in ["Yes", "yes", "Y", "y"]:
        run()
    elif repeat in ["No", "no", "N", "n"]:
        print("Okay, Goodbye.")
    else:
        print("I'm sorry, I didn't understand that. Please answer a yes or a no.")
        rep()
#       Put a limit on how many times the function runs after an invalid answer?

run()