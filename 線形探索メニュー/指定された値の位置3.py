# coding: utf-8
##パターン1
import sys
tmp = [i.split() for i in sys.stdin.readlines()]
n = tmp[0][0]
k = tmp[2][0]

index = 1
for i in tmp[1]:
    if i == k:
        print(index)
    else:
        pass
    index += 1

# ##パターン2
# n = input()
# tmp = input().split()
# k = input()
# index = 1
# for i in tmp:
#     if i == k:
#         print(index)
#     else:
#         pass
#     index += 1