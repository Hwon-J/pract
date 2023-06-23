import sys
sys.setrecursionlimit(10000000)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1] * m for _ in range(n)]

directy = [1, -1, 0, 0]
directx = [0, 0, 1, -1]

def dfs(y, x):
    if y == 0 and x == 0: 
        return 1

    if dp[y][x] != -1:  
        return dp[y][x]

    dp[y][x] = 0  

    for i in range(4):
        dy = y + directy[i]
        dx = x + directx[i]

        if 0 <= dy < n and 0 <= dx < m and arr[dy][dx] > arr[y][x]:
            dp[y][x] += dfs(dy, dx)

    return dp[y][x]

print(dfs(n - 1, m - 1))
