# -*- coding: utf-8 -*-
"""
@author: WyldPhyr
"""

while True:
    start = raw_input("Enter the text you would like reversed: ")
    rev = start[::-1]
    print rev
    rerun = raw_input("Would you like to reverse another text? " )
    if rerun in ["Yes", "yes", "y", "Y"]:
        print("Okay")
    else:
        break
print("Goodbye.")        