# -*- coding: utf-8 -*-
"""
Created on Fri May  4 23:34:35 2018

@author: Maziar
"""

text = []
i = 1
avg = 0
while text != 'stop':
    text = input("Enter numbers for which the moving average will be calculated: ")  # Python 3
    avg = (avg * (i-1) + int(text)) / i
    i += 1
    print(avg)