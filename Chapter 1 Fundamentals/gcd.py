# -*-coding: utf-8 -*-
# Author:
# 欧几里得算法，求两个数的最大公约数；

def gcd(p, q):
    if q == 0:
        return p
    r = p % q
    return gcd(q, r)

print(gcd(6, 6))