# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 13:45:29 2016

@author: WyldPhyr
"""

def down():
    numb = [99, 98, 97, 96, 95]
    while not min(numb) == 0:
        numb.append(min(numb) - 1)
    for word in numb:
        num = str(word)
        base1 = num + " Bottles of beer on the wall, " + num
        base2 = " bottles  of beer, take one down, pass it around, " + num
        base3 = "  Bottles of beer on the wall."
        if word >= 10:
            base4 = "**" * 30
        else:
            base4 = "**" * 32
        print(base1 + base2 + base3 + base4)
down()
