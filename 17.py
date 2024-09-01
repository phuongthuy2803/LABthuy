# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:56:10 2024

@author: MSI GAMING
"""

x= input("Nhập 3 số nguyên (a, b, c): ")
a, b, c= map(int, x.split(","))
print("Số lớn nhất là ", max(a, b,c))
print("Số nhỏ nhất là ", min(a, b, c))