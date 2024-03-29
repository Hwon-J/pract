n, k = map(int, input().split())
mod=1000000000
dp = [[0] * (n + 1) for _ in range(k + 1)]
dp[0][0] = 1

for i in range(1, k + 1):
    for j in range(n + 1):
        dp[i][j] = sum(dp[i - 1][:j + 1]) % mod

print(dp[k][n])