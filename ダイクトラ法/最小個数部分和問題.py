import sys
tmp = sys.stdin.readlines()
A = int(tmp[0])
s = list(map(int, tmp[1].split()))
# print(s)
N = len(s)
# print(N)

inf = float("Inf")
dp = [[inf for _ in range(A + 1)] for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
  for j in range(A + 1):
    if j >= s[i]:
      # print(dp)
      dp[i+1][j] = min(dp[i][j-s[i]] + 1, dp[i][j])
    else:
      dp[i+1][j] = dp[i][j]

if dp[N][A] == inf:
  dp[N][A] = -1

print(dp[N][A])