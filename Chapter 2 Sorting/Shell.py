# -*-coding: utf-8 -*-
# Author:
# 希尔排序

import random

def Shell(lst):
    N = len(lst)
    h = 1
    while h < N/3:
        h = 3*h +1
    while h >= 1:
        for i in range(h, N):
            for j in range(i,h-1,-h):
                if lst[j] < lst[j-h] and j>=h:
                    lst[j], lst[j-h] = lst[j-h],lst[j]
        h = h//3
    return lst

# test
l = list("0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T".split())
random.shuffle(l)
print(l)
print(Shell(l))