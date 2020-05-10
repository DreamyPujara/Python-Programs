# -*- coding: utf-8 -*-
"""
hackerrank problem challenge:
    to check the given year is leap year or not

@author: dreamy
"""
def is_leap(year):
    leap=False
    if year%400==0:
        leap=True
    elif year%100==0:
        leap=False
    elif year%4==0:
        leap=True
    return leap

year=int(input())
print (is_leap(year))
