# coding: utf-8
import sys
tmp = [i.split() for i in sys.stdin.readlines()]
n = int(tmp[0][0])
a = list(map(int, tmp[1]))
# a = [int(j) for j in tmp[1]]

#A[i] を、整列済みの A[0] ~ A[i-1] の適切な位置に挿入する
for i in range(1, n):
    #実装の都合上、A[i] の値が上書きされてしまうことがあるので、予め A[i] の値をtmpにコピーしておく
    tmp = a[i]
    #tmpの適切な挿入位置を表す変数 j を用意
    j = i-1
    #tmpの適切な挿入位置が見つかるまで、tmpより大きい要素を1つずつ後ろにずらしていく
    while j >= 0 and a[j] > tmp:
            a[j+1] = a[j]
            j -= 1
    #tmp を挿入    
    a[j+1] = tmp
    #A[0] ~ A[i] が整列済みになった
    print(" ".join(list(map(str, a))))