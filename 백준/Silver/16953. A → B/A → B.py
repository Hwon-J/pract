from collections import deque

a, b = map(int, input().split())
flag = 0
q = deque([(a, 1)])
while q:
    num, cnt = q.popleft()
    if num == b:
        print(cnt)
        flag = 1
        break
    if num * 2 <= b:
        q.append((num * 2, cnt + 1))
    if (num * 10) + 1 <= b:
        q.append(((num * 10) + 1, cnt + 1))
if not flag:
    print(-1)