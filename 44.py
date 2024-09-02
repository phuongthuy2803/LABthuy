# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:39:20 2024

@author: MSI GAMING
"""

n= int(input("Nhập số nguyên n: "))
while n <= 0:
    n= int(input("Nhập số nguyên n: "))
S = 0
for i in range(0, n+1):
    S+=(((2*i)+1)/((2*i)+2))
print("S = ", S)