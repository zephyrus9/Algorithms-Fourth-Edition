# -*-coding: utf-8 -*-
# Author:
# 选择排序

import random

def Selection(lst):
    N = len(lst)
    for i in range(N):
        min = i
        for j in range(i+1,N):
            if lst[j] < lst[min]:
                min = j
        lst[min], lst[i] = lst[i], lst[min]
    return lst


# test
l = list("0 1 2 3 4 5 6 7 8 9 A B C D E F G H I J K L M N O P Q R S T".split())
random.shuffle(l)
print(l)
print(Selection(l))