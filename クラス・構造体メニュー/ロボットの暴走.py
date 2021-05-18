# coding: utf-8
import sys
tmp = [i.split() for i in sys.stdin.readlines()]
H = int(tmp[0][0]) #y座標
W = int(tmp[0][1]) #x座標
N = int(tmp[0][2]) #ロボットの数
K = int(tmp[0][3]) #ロボットの移動回数

o_list = []
for j in range(1, 11):
  x = int(tmp[j][0])
  y = int(tmp[j][1])
  o_list.append([x, y])

robot_list = []
for j in range(11, 11 + N):
  x = int(tmp[j][0])
  y = int(tmp[j][1])
  level = int(tmp[j][2])
  robot_list.append([x, y, level])

hoge = []
for j in range(11 + N, 11 + N + K):
  robot_id = int(tmp[j][0])
  toward = tmp[j][1]
  hoge.append([robot_id, toward])
  
  #ロボットを動かす
  #Lv1:1, Lv2:2, Lv3:5, Lv4:10マス移動することに注意
  level = robot_list[robot_id - 1][2]
  if level< 3:
    step = level
  elif level == 3:
    step = 5
  elif level >= 4:
    step = 10
  
  #方角を考慮する
  if toward == "N":
    robot_list[robot_id-1][1] -= step
  elif toward == "S":
    robot_list[robot_id-1][1] += step
  elif toward == "W":
    robot_list[robot_id-1][0] -= step
  else:
    robot_list[robot_id-1][0] += step
  
  #障害物と一致したら、レベルを1つ上げる
  if [robot_list[robot_id-1][0], robot_list[robot_id-1][1]] in o_list:
    robot_list[robot_id-1][2] += 1

#ロボットの位置とレベルを表示する
for k in range(0, len(robot_list)):
  r = robot_list[k]
  print(f"{r[0]} {r[1]} {r[2]}")
  
##class使おうと思ったが、うまくできず。
# class Obstacle:
#   def __init__(self, x, y):
#     self.x = x
#     self.y = y

# class Robot():
#   status = []
#   def __init__(self, x, y, level):
#     self.x = x
#     self.y = y
#     self.status = x,y, level
