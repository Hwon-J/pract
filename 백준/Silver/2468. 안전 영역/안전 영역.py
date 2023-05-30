import sys
input = sys.stdin.readline
sys.setrecursionlimit(1000000)

N = int(input())
arr =[]
# 최고 높이
high = 0

for _ in range(N):
    lst = list(map(int, input().split()))
    high = max(max(lst),high)
    arr.append(lst)


# 물에 잠기지 않는 영역 개수 최소 1
mx = 1

directy = [1, -1, 0, 0]
directx = [0, 0, 1, -1]

def dfs(i,j,num):
    for k in range(4):
        dy, dx = i+directy[k], j+directx[k]
        if 0<= dy <N and 0<= dx <N and visit[dy][dx]==0 and arr[dy][dx]>num:
            visit[dy][dx]=1
            dfs(dy,dx,h)



for h in range(1, high):
    visit = [[0] * N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > h and visit[i][j] == 0:
                cnt += 1
                visit[i][j] = 1
                dfs(i,j,h)
    mx = max(cnt,mx)

print(mx)