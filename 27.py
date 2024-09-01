# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 12:04:53 2024

@author: MSI GAMING
"""

import math
h= input("Nhập hình (n, v, t): ")
if h == "v":
    print("Tính P và S của hình vuông")
if h == "n":
    print("Tính P và S của hình chữ nhật")
if h == "t":
    print("Tính P và S của hình tròn")
d= float(input("Nhập chiều dài (nếu là hình tròn nhập 0) = "))
r= float(input("Nhập chiều rộng (bán kính hình tròn) = "))
if h == "v":
    print("Kết quả P = ", 4*d, "\tS = ", d**2)
elif h == "n":
    print("Kết quả P = ", (r+d)*2, "\tS = ", d*r)
elif h == "t":
    print("Kết quả P = ", 2*math.pi*r, "\tS = ", math.pi*(r**2))
