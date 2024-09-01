# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 16:51:32 2024

@author: MSI GAMING
"""

n= int(input("Nhập số N nguyên dương: "))
while n <= 0:
    n= int(input("Nhập lại số N NGUYÊN DƯƠNG: "))
for x in range(1,n+1):
    if n % x == 0:
        print(x, end="\t")