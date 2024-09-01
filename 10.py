# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:17:20 2024

@author: MSI GAMING
"""

x= int(input("Số xe của bạn (gồm 4 chữ số): "))
if x>=1000 and x<10000:
    a= x//1000
    b= (x%1000)//100
    c= (x%100)//10
    d= x%10
    y= a+b+c+d
    print("Số nút: ", y%10)
else:
    print("Số xe không hợp lệ!")