# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 15:46:01 2024

@author: MSI GAMING
"""

n= int(input("Nhập số nguyên n: "))
x= float(input("Nhập số nguyên x: "))
while n <= 0:
    n= int(input("Nhập số nguyên n: "))
S = x
for i in range(2, n+1):
    S+=((x**i)/((i*(i+1))//2))
print("S = ", S)