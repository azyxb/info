#!/usr/bin/env python3

def gcd(a, b):
    if a == 0 :
        return b
    return gcd(b%a, a) 

a = 12000
b = 8642
print(gcd(a, b))
