import sys
_input = '''
3 2 10
7 5 3
'''
#######################################################
#入力パターン1
tmp = [i.split() for i in sys.stdin.readlines()]
n, K, A = list(map(int, tmp[0]))
# print(n, K, A)
l = list(map(int, tmp[1]))
# print(l)

##入力パターン2
# n, K, A =list(map(int, input().split()))
# print(n, K, A)
# l = list(map(int, input().split()))
# print(l)
#######################################################

####################※一番下のやり方だと計算量が多い########################
####################↓これが望ましい（最小個数部分和問題と同様の解法）↓########################
inf = float("inf")
dp = [[inf for _ in range(A + 1)] for _ in range(n + 1)]
dp[0][0] = 0
# print(dp)

for i in range(n):
  for j in range(A+1):
    if l[i] <= j:
        dp[i+1][j] = min(dp[i][j - l[i]] + 1, dp[i][j] + 1)
    else:
      dp[i+1][j] = dp[i][j]

# print(dp)
if dp[n][A] <= K:
  print("YES")
else:
  print("NO")
#######################################################


# # ####################↓これだと計算量が多い↓########################
# dp = [[0 for _ in range(A + 1)] for _ in range(n + 1)]
# dp[0][0] = 1
# # print(dp)

# A_list = [] #パターンBで回答する場合

# for i in range(n):
#   for j in range(A+1):
#     if l[i] <= j:
#       if dp[i][j - l[i]] < 1:
#         dp[i+1][j] = max(dp[i][j - l[i]], dp[i][j])
#       else:
#         dp[i+1][j] = max(dp[i][j - l[i]] + 1, dp[i][j] + 1)
#     else:
#       dp[i+1][j] = dp[i][j]
#   A_list.append(dp[i+1][A]) #パターンBで回答する場合

# # print(dp)

# # #パターンA
# # is_no = True
# # for i in range(n+1):
# #   if dp[i][A] == K + 1:
# #     print("YES")
# #     is_no = False
# #     break
  
# # if is_no:
# #   print("NO")

# #パターンB
# # print(A_list)
# if K + 1 in A_list:
#   print("YES")
# else:
#   print("NO")
# #######################################################
