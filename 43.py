# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:37:00 2024

@author: MSI GAMING
"""

n= int(input("Nhập số nguyên n: "))
while n <= 0:
    n= int(input("Nhập số nguyên n: "))
S = 0
for i in range(1, n+1):
    S+=(i/(i+1))
print("S = ", S)