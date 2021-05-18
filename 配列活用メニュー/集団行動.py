# coding: utf-8
_sample_input = '''
100 5
resize 29
reverse
swap 18 24
resize 47
reverse
'''

import sys
tmp = [i.split() for i in sys.stdin.readlines()]
N = int(tmp[0][0])
Q = int(tmp[0][1])

num_list = [j for j in range(1, N+1)]

for k in range(1, Q+1):
  list_len = len(tmp[k])
  if list_len == 1:
    num_list = num_list[::-1]
  elif list_len == 2:
    C = int(tmp[k][1])
    try:
      num_list = num_list[:C]
    except:
      pass
  else:
    A = int(tmp[k][1]) - 1
    B = int(tmp[k][2]) - 1
    # num_list[A], num_list[B] = num_list[B], num_list[A]
    tmp_num = num_list[A]
    num_list[A] = num_list[B]
    num_list[B] = tmp_num
for l in num_list:
  print(l)

