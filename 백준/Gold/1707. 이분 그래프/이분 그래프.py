from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    arr = [[] for _ in range(V+1)]
    visit = [0]*(V+1)
    # 인접리스트 구하기
    for _ in range(E):
        a, b = map(int, input().split())
        arr[a].append(b)
        arr[b].append(a)
    flag = 1
    def bfs(st):
        global flag
        q= deque()
        q.append(st)
        visit[st]=1
        while q:
            now = q.popleft()
            for i in arr[now]:
                if visit[i]==0:
                    q.append(i)
                    if visit[now]==1:
                        visit[i]=2
                    elif visit[now]==2:
                        visit[i]=1
                elif visit[now]==visit[i]:
                    flag=0


    for i in range(1, V+1):
        if visit[i]==0:
            bfs(i)

    if flag:
        print('YES')
    else:
        print('NO')