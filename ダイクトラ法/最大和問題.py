import sys
tmp = sys.stdin.readlines()
N = int(tmp[0])
a = list(map(int, tmp[1].split()))

dp = [0] * (N + 1)
for i in range(N):
  dp[i + 1] = max(dp[i], dp[i] + a[i])