# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:20:07 2024

@author: MSI GAMING
"""

def ktrso(n):
    if n % 2 != 0 and n < 0:
        return -1
    elif n % 2 == 0 and n > 0:
        return 1
    return 0
n= int(input("Nhập số n: "))
print(f"{ktrso(n)}")