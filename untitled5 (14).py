# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1d4v8EUsWtm02DDz-u4yAcRVzoVlkISQB
"""

def majmoe(i):
   sum=0
   while i != 0:
     sum +=i%10
     i//=10
   return sum

def function1(n):
  for I in range (n):
    k=majmoe(i)
    if k==n:
      return k
  return print ("not find")