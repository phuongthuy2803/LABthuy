# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 11:31:05 2024

@author: MSI GAMING
"""

N= int(input("Nhập số nguyên dương N có 2 chữ số: "))
if N>=10 and N<=99:
    x= N//10
    y= N%10
    print("Tổng các chữ số của N là ", x+y)
else:
    print("Nhập lại số nguyên dương N có 2 chữ số!")