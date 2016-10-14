# -*- coding: utf-8 -*-
"""
@author: WyldPhyr
"""

while True:
    start = raw_input("Enter the word you would like translated from pig latin: ")
    frst = start[-3]
    base = start[:-3]
#   :)
    print frst + base
    rerun = raw_input("Would you like to translate another word? " )
    if rerun in ["Yes", "yes", "y", "Y"]:
        print("Okay")
    else:
        break
print("Goodbye.")        