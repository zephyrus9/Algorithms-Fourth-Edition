# -*-coding: utf-8 -*-
# Author:
# 插入排序

import random

def Insertion(lst):
    N = len(lst)
    for i in range(1,N):
        for j in range(i,0,-1):
            if lst[j] < lst[j-1]:
                lst[j], lst[j-1] = lst[j-1], lst[j]
    return lst

# test
l = list("0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T".split())
random.shuffle(l)
print(l)
print(Insertion(l))