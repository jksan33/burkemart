# -*- coding: utf-8 -*-
"""
@author: WyldPhyr
"""

while True:
    start = raw_input("Enter the word you would like translated into pig latin: ")
    frst = start[0]
    base = start[1:]
    ay = "ay"
    print base + frst + ay
    rerun = raw_input("Would you like to translate another word? " )
    if rerun in ["Yes", "yes", "y", "Y"]:
        print("Okay")
    else:
        break
print("Goodbye.")        
