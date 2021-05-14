# coding: utf-8
import sys
tmp = [i.split() for i in sys.stdin.readlines()]
n = int(tmp[0][0])
a = [int(j) for j in tmp[1]]

for i in range(0, n-1):
  #for文を逆順で回す
  for j in reversed(range(i + 1, n)):
    if a[j-1] > a[j]:
      #前後の数字を入れ替え
      a[j-1], a[j] = a[j], a[j-1]
  print(" ".join(list(map(str, a))))