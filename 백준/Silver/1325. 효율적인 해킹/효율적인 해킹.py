from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
rlt = []

for _ in range(M):
    A, B = map(int, input().split())
    arr[B].append(A)

def bfs(st):
    visit = [0] * (N + 1)
    cnt = 0
    q = deque()
    q.append(st)
    visit[st]=1
    while q:
        now= q.popleft()
        for i in arr[now]:
            if not visit[i]:
                visit[i] = 1
                cnt+=1
                q.append(i)
    return cnt

mx = 0
for i in range(1, N+1):
    ans = bfs(i)
    if mx < ans:
        mx = ans
        rlt.clear()
        rlt.append(i)
    elif mx == ans:
        rlt.append(i)
print(*rlt)