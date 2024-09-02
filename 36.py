# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:46:13 2024

@author: MSI GAMING
"""

n= int(input("Nhập số n nguyên và lớn hơn 0: "))
while n <= 0:
    n= int(input("Nhập số n nguyên và lớn hơn 0: "))
S = 0
for i in range(1, n+1):
    S+=(i**2)
print(S)