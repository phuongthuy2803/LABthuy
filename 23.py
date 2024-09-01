# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 21:34:30 2024

@author: MSI GAMING
"""

import math
print("Giải và biện luận phương trình bậc hai: ax^2 + bx + c = 0")
a= float(input("Nhập hệ số a: "))
b= float(input("Nhập hệ số b: "))
c= float(input("Nhập hệ số c: "))
if a==0:
    if b==0:
        if c==0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        if c==0:
            print("Phương trình có nghiệm bằng 0")
        else:
            print("Phương trình có nghiệm bằng", -c/b)
else:
    delta = (b ** 2) - (4 * a * c)
    if delta<0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        print("Phương trình có nghiệm kép bằng ", -b / (2 * a))
    else:
        print("Phương trình có 2 nghiệm phân biệt")
        print("x1 = ", (-b - math.sqrt(delta)) / (2 * a))
        print("x2 = ", (-b + math.sqrt(delta)) / (2 * a))