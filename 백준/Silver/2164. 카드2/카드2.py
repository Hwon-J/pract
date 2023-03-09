from collections import deque
N=int(input())
q=deque()
for i in range(N):
    q.append(i+1)

while len(q)>1:
    q.popleft()
    tm=q.popleft()
    q.append(tm)

print(q[0])