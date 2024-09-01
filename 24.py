# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 10:49:52 2024

@author: MSI GAMING
"""

x= int(input("Nhập giờ:"))
y= int(input("Nhập phút: "))
z= int(input("Nhập giây: "))
if 0<=x<=24 and 0<=y<=60 and 0<=z<=60:
    print("Thời gian hợp lệ")
else:
    print("Thời gian không hợp lệ")