# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 12:37:49 2024

@author: MSI GAMING
"""

def cong(n):
    s = 0
    for i in range(1, n+1):
        s +=i
    return s
def phso(n):
    q = 0
    for i in range(1, n+1):
        q += (1/i)
    return q
def nhan(n):
    m= 1
    for i in range(1, n+1):
        m*= i 
    return m
def githua(n):
    t= 0
    for i in range(1, n+1):
        t+= nhan(i)
    return t
n= int(input("Nhập số nguyên n: "))
while n<0:
    n= int(input("Nhập số nguyên n: "))
print(f"a bằng {cong(n)} \nb bằng {phso(n)} \nc bằng {githua(n)} \nd bằng {nhan(n)} ")