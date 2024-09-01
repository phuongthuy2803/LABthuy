# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:46:19 2024

@author: MSI GAMING
"""

n= int(input("Nhập số N nguyên dương: "))
while n <= 0:
    n= int(input("Nhập lại số N NGUYÊN DƯƠNG: "))
m= str(n)
t= 0
for i in m:
    t+= int(i)
print(f"Tổng các chữ số trong {n} là {t}")
