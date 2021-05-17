import sys
tmp = [i.split() for i in sys.stdin.readlines()]
h,w = list(map(int, tmp[0]))
first_row = list(map(int, tmp[1]))
#例外処理
if h < 2:
  second_row = [0,0,0]
else:
  second_row = list(map(int, tmp[2]))
if w < 3:
  tmp[1].append(0)
  tmp[1].append(0)

ans = first_row[0] + first_row[1] * 2 + first_row[2] + second_row[1] + second_row[2]
print(ans)