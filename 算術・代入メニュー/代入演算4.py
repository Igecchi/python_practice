# coding: utf-8
import sys
N = 10_000
a, b = list(map(int, sys.stdin.readline().split()))
N = int(N / a)
N = N % b
print(N)