# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:49:29 2024

@author: MSI GAMING
"""

n= int(input("Nhập số nguyên n chẵn và lớn hơn 0: "))
while n <= 0 or n % 2 != 0:
    n= int(input("Nhập số nguyên n chẵn và lớn hơn 0: "))
S = 0
for i in range(2, n+1, 2):
    S+=i
print(S)