# coding: utf-8
import sys
##パターン1
#標準入力が複数行あり、その一行目を扱いたい場合
# tmp = [i.split() for i in sys.stdin.readlines()]
# a, b, c, d = list(map(int, tmp[0]))

##パターン2
#map関数は[]ではなく、list()を使って明示的にリスト化する必要あり
a, b, c, d = list(map(int, sys.stdin.readline().split()))

ans = (( a + b ) * c ) ** 2 % d
print(ans)