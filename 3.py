# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:15:31 2024

@author: MSI GAMING
"""

a= int(input("Nhập số nguyên dương a: "))
b= int(input("Nhập số nguyên dương b: "))

if a>0 and b>0:
    print(f"Phép chia lấy dư của {a} và {b} bằng ", a%b)
    print(f"Phép chia lấy nguyên của {a} và {b} bằng ", a//b)
else:
    print("Vui lòng nhập số a và b NGUYÊN DƯƠNG")    