# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 16:09:43 2024

@author: MSI GAMING
"""

def ktrso(n):
    if n % 2 ==0 and n < 0:
        return True
    return False
n= int(input("Nhập số n: "))
print(f"{n} có phải là sô chẵn âm: {ktrso(n)}")