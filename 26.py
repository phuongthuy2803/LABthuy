# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 11:28:48 2024

@author: MSI GAMING
"""

#câu a
a= int(input("Nhập số a: "))
b= int(input("Nhập số b: "))
c= int(input("Nhập số c: "))
if a>b:
    a,b = b,a
if a>c:
    a,c = c,a
if b>c:
    b,c = c,b
print(f"Các số {a}, {b}, {c} theo thứ tự tăng dần là ", a,b,c)



#câu b
n= int(input("Nhập số nguyên: "))
chuoin= str(n)
sxn= ''.join(sorted(chuoin))
N= int(sxn)
print("Số có các con số theo thứ tự tăng dần là: ", N)