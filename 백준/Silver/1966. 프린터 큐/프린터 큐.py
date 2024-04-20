from collections import deque

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    q = deque()
    for i in range(len(priorities)):
        q.append((i, priorities[i]))
    cnt = 0
    while q:
        mx = max(q, key=lambda x: x[1])[1]
        tm = q.popleft()
        if tm[1] < mx:
            q.append(tm)
        else:
            cnt += 1
            if tm[0] == m:
                print(cnt)
                break

                