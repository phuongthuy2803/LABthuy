# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 12:56:11 2024

@author: MSI GAMING
"""

t= input("Nhập thời gian đầu (hh:mm:ss): ")
g= input("Nhập thời gian sau (hh:mm:ss): ")
h1, m1, s1= map(int, t.split(":"))
h2, m2, s2= map(int, g.split(":"))
a= h1*3600 + m1*60 + s1
b= h2*3600 + m2*60 + s2
if a>b:
    x= h1 - h2
    y= m1 - m2
    z= s1 - s2
    m= h1 + h2
    n= m1 + m2
    l= s1 + s2
    print(f"Tổng thời gian 2 giờ: {m}:{n}:{l} \nHiệu thời gian 2 giờ: {x}:{y}:{z}")
elif a<b:
    m= h1 + h2
    n= m1 + m2
    l= s1 + s2
    print(f"Tổng thời gian 2 giờ: {m}:{n}:{l} \nHiệu thời gian 2 giờ: ",h2 - h1,":",m2 - m1,":",s2 - s1)
else:
    m= h1 + h2
    n= m1 + m2
    l= s1 + s2
    print(f"Tổng thời gian 2 giờ: {m}:{n}:{l} \nHiệu thời gian 2 giờ: 0")