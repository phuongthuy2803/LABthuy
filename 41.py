# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:18:39 2024

@author: MSI GAMING
"""

n= int(input("Nhập số nguyên n: "))
while n <= 0:
    n= int(input("Nhập số nguyên n: "))
S = 0
for i in range(1, (2*(n+1))+1, 2):
    S+=(1/i)
print("S = ", S)