# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:35:59 2024

@author: MSI GAMING
"""

a= int(input("Nhập cạnh a: "))
b= int(input("Nhập cạnh b: "))
c= int(input("Nhập cạnh c: "))
while a <=0 or b<=0 or c<=0:
    a= int(input("Nhập lại cạnh a: "))
    b= int(input("Nhập lại cạnh b: "))
    c= int(input("Nhập lại cạnh c: "))
if a+b>c and a+c>b and b+c>a:
  if a==b and b==c:
      print("a,b,c là 3 cạnh của tam giác đều")
  elif a==b or a==c or b==c:
      print("a,b,c là 3 cạnh của tam giác cân")
  elif a**2+b**2==c**2 or a**2+c**2==b**2 or a**2==b**2+c**2:
      print("a,b,c là 3 cạnh trong tam giác vuông")
  else:
      print("a,b,c là 3 cạnh trong tam giác thường")
else:
    print("a,b,c không phải là 3 cạnh trong tam giác")