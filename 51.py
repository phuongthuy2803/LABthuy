# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:04:51 2024

@author: MSI GAMING
"""

def so(n):
    while n < -89 or n > 90:
        n= int(input("Nhập lại số n: "))
    return "Số thuộc đoạn [-89;90]"
n= int(input("Nhập số n thuộc đoạn [-89;90]: "))
print(f"{so(n)}")