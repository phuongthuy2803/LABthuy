# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 12:10:47 2024

@author: MSI GAMING
"""

n= int(input("Nhập số nguyên dương n: "))
while n <= 0:
    n= int(input("Nhập lại số nguyên dương n: "))
if n==1:
    print("1 không phải là số nguyên tố")
elif n==2:
    print("2 là số nguyên tố")
else:
    snt = False
    for i in range(2, n-1):
        if n % i == 0:
           snt = True
           break
    if snt:
           print(f"{n} không phải là số nguyên tố")
    else:
       print(f"{n} là số nguyên tố")