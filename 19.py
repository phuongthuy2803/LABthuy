# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 18:42:13 2024

@author: MSI GAMING
"""

a= int(input("Nhập số nguyên a: "))
b= int(input("Nhập số nguyên b: "))
c= int(input("Nhập số nguyên c: "))
d= int(input("Nhập số nguyên d: "))
nho= a
if b<a:
    nho= b
if c<a:
   nho= c
if d<a:
    nho= d
print(f"Số nhỏ nhất là {nho}")