N, K = map(int, input().split())
bags = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*(K+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(K+1):
        weight, value = bags[i-1]
        if weight <= j:
            dp[i][j] = max(dp[i-1][j], value + dp[i-1][j-weight])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[N][K])
