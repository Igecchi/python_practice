# coding: utf-8

##パターン1
import sys
tmp = [i.split() for i in sys.stdin.readlines()]
n = int(tmp[0][0])
k = int(tmp[n+1][0])
l = int(tmp[n+1][1])
for j in range(1, n+1):
    if k <= int(tmp[j][1]) <= l:
        print(tmp[j][0])
    else:
        pass

##パターン2    
# n = int(input())
# all_list = []
# for i in range(0, n):
#     all_list.append(input().split())
# s = list(map(int, input().split()))
# k = s[0]
# l = s[1]

# for j in range(0, len(all_list)):
#     if k <= int(all_list[j][1]) <= l:
#         print(all_list[j][0])
#     else:
#         pass