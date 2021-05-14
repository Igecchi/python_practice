# coding: utf-8
import sys
a = [i.split() for i in sys.stdin.readlines()]
n = int(a[0][0])
num_list = list(map(int,a[1]))

for j in range(0, len(num_list)-1):
    #未整列部分から最小値を見つける
    #その最小値と整列済み+1個目の数字を入れ替える
    tmp = num_list[j]
    min_num = min(num_list[j:])
    ## パターンA ##
    #最小値について、リスト内重複を避けられるようにする
    min_index = num_list[j:].index(min_num) + j
    num_list[j] = min_num
    num_list[min_index] = tmp
    
    # ## パターンB ##
    # min_index = j
    # for k in range(j+1, n):
    #     if num_list[k] < num_list[min_index]:
    #         min_index = k
    # num_list[j], num_list[min_index] = num_list[min_index], num_list[j]
    
    print(' '.join(list(map(str, num_list))))