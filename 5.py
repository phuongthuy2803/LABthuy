# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 12:37:52 2024

@author: MSI GAMING
"""

x= input("Nhập thời gian theo định dạng hh:mm:ss ")
hh, mm, ss= map(int, x.split(":"))
y= (hh*3600)+(mm*60)+ss
print(f"Tổng số giây là {y}")