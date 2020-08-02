#! /usr/bin/env python

#리스트[ 1, 1, 2, 0, 0, 2, 3, 3] 에서 
#가장 큰 값과 가장 작은 값을 구해보세요

l = [3, 1, 1, 2, 4, 0, 0, 2, 3, 3]

max_val = l[0]
min_val = l[0]

for elem in l:
    if elem > max_val:
        max_val = elem 
    if elem < min_val:
        min_val = elem

print("가장 큰 값:",max_val,"가장 작은 값:", min_val)
        




