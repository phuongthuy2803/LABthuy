# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:59:01 2024

@author: MSI GAMING
"""

thang = int(input("Nhập tháng (1-12): "))
while thang < 1 or thang >12:
    thang = int(input("Nhập lại tháng (1-12): "))
nam = int(input("Nhập năm: "))
if (nam % 4 == 0 and nam % 100 != 0) or nam % 400 == 0:
    print("Năm nhuận")
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        print("Tháng", thang, "có 31 ngày")
    elif thang in [4,6,9,11]:
        print("Tháng", thang, "có 30 ngày")
    elif thang in [2]:
        print("Tháng 2 có 29 ngày")
else:
    print("Năm không nhuận")
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        print("Tháng", thang, "có 31 ngày")
    elif thang in [4,6,9,11]:
        print("Tháng", thang, "có 30 ngày")
    elif thang in [2]:
        print("Tháng 2 có 28 ngày")