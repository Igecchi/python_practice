# coding: utf-8
_sample_input = '''
5 3
1
2
3
4
5
'''

import sys
tmp = [i.split() for i in sys.stdin.readlines()]
N = int(tmp[0][0])
K = int(tmp[0][1])

for j in range(1, N+1):
  B_ = int(tmp[j][0])
  if B_ >= K:
    print(B_)