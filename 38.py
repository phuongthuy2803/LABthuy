# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 13:31:37 2024

@author: MSI GAMING
"""

n= int(input("Nhập số nguyên dương lẻ cần tính giai thừa: "))
S= 1
while n <= 0 or n%2 == 0:
    n= int(input("Vui lòng nhập số NGUYÊN DƯƠNG LẺ: "))
for i in range(1, n+1):
    if n == 1:
        print("KQ = 1")
    elif n > 1:
        S*= i
print("KQ = ", S)      