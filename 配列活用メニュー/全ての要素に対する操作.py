# coding: utf-8
_sample_input = '''
5 100
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
  print(K + int(tmp[j][0]))