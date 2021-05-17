# coding: utf-8
##パターン1
# import sys
# tmp = [i.split() for i in sys.stdin.readlines()]
# n = int(tmp[0][0])
# num = list(map(int, tmp[1]))

##パターン2
n = int(input())
num = list(map(int, input().split()))

num_min = min(num)
num_max = max(num)
print(f"{num_max} {num_min}")