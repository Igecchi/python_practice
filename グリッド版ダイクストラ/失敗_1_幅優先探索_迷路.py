import sys
tmp = [i.split() for i in sys.stdin.readlines()]
h,w = list(map(int, tmp[0]))
count = 1
x = 0
y = 1
is_on = True

#右に動く
def right():
  global x, y
  is_right = True
  while is_right:
    try:
      if tmp[y][x+1] == "0":
        count += 1
        x += 1
        print("右")
      else:
        down()
        is_right = False
    except:
      down()
      is_right = False

#下に動く
def down():
  global x, y
  is_down = True
  while is_down:
    try:
      if tmp[y+1][x] == "0":
        count += 1
        y += 1
        print("した")
      else:
        right()
        is_down = False
    except:
      right()
      is_down = False

#上に動く
def up():
  global x, y
  is_up = True
  while is_up:
    try:
      if tmp[y-1][x] == "0":
        count += 1
        y -= 1
        print("↑")
        right()
      else:
        is_up = False
    except:
      is_up = False

#左に戻って下に動く
def left_down():
  global x, y
  if tmp[y-1][x-1] == "0":
    x -= 1
    y -= 1
    print("左下")

while is_on:
  if x >= w - 1 and y >= h:
    count += 1
    is_on =False
  else:
    right()
print(count)