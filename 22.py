# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:24:58 2024

@author: MSI GAMING
"""

print("Giải và biện luận phương trình bậc nhất ax + b = 0")
a=float(input("Nhập hệ số a: "))
b=float(input("Nhập hệ số b: "))
if a==0 and b==0:
    print("Phương trình vô số nghiệm")
elif a==0 and b!=0:
    print("Phương trình vô nghiệm")
else:
    print("Phương trình có nghiệm bằng ", -b/a)