T = int(input())
dp = [0] * 42
dp[0] = [1, 0]
dp[1] = [0, 1]

for i in range(2, 42):
    dp[i] = (dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1])

for _ in range(T):
    n = int(input())
    print(dp[n][0], dp[n][1])