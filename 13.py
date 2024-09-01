# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 20:31:03 2024

@author: MSI GAMING
"""

d= input("Nhập ngày tháng năm sinh của bạn theo định dạng dd mm yyyy: ")
b= d.replace(" ", "/")
print(b)
i= b[0:5]+b[7:9]
print(i)
dd, mm, yyyy= map(int, b.split("/"))
print(f"{yyyy}/{mm}/{dd}")
n= input("Nhập ngày tháng năm sinh của bạn theo định dạng yyyy mm dd: ")
r= n.replace(" ", "/")
print(r)
t= n[0:5]+n[7:9]
print(t)
y, m, d= map(int, r.split("/"))
print(f"{d}/{m}/{y}")