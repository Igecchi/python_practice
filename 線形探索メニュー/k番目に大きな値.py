# coding: utf-8

##パターン1
import sys
tmp = [i.split() for i in sys.stdin.readlines()]
n = int(tmp[0][0])
k = int(tmp[2][0])
num_sorted = sorted(list(map(int, tmp[1])))
print(num_sorted[-k])

##パターン2
# n = int(input())
# num_sorted = sorted(map(int, input().split()))
# k = int(input())
# print(num_sorted[-k])