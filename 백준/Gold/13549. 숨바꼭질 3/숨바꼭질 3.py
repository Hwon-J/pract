from collections import deque

def bfs(n, k):
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            return visit[x]

        for i in (x-1, x+1, 2*x):
            if 0 <= i <= 100000 and visit[i] == 0:
                if i == x * 2 and i != 0:
                    visit[i] = visit[x]
                    q.appendleft(i)
                else:
                    visit[i] = visit[x] + 1
                    q.append(i)


n, k = map(int, input().split())
visit = [0] * 100001

print(bfs(n, k))
