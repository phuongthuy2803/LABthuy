# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 11:55:23 2024

@author: MSI GAMING
"""

import math
n= int(input("Nhập số nguyên dương N: "))
while n<=0:
    n= int(input("Nhập lại số nguyên dương N: "))
if math.sqrt(n)**2 == n:
    print(f"{n} là số chính phương")
else:
    print(f"{n} không phải là số chính phương")