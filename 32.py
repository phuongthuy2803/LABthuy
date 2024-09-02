# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:47:51 2024

@author: MSI GAMING
"""

x= float(input("Nhập quảng đường đã đi (km): "))
if x<=1:   
  print("Phí taxi của bạn là (ngàn đồng): ", 15*x)
elif x>=2 and x<=5:
    print("Phí taxi của bạn là (ngàn đồng): ", 15 + 13.5*(x-1))
elif x>=6 and x<= 120:
    print("Phí taxi của bạn là (ngàn đồng): ", 15 + 13.5*4 + 11*(x-5))
elif x>120:  
    print("Phí taxi của bạn là (ngàn đồng): ",(15 + 13.5*4 + 11*(x-5))*0.9)