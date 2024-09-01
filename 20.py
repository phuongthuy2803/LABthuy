# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:16:52 2024

@author: MSI GAMING
"""

a= int(input("Nhập số nguyên a: "))
b= int(input("Nhập số nguyên b: "))
c= int(input("Nhập số nguyên c: "))
lon= a
if b>a:
    lon= b
if c>a:
   lon= c
print(f"Số lớn nhất là {lon}")