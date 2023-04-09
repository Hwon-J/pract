from collections import deque
import sys
input = sys.stdin.readline
q= deque()
N = int(input())
for _ in range(N):
    a = input()
    if 'push' in a:
        tm = a[5:-1]
        q.append(tm)
    elif 'pop' in a:
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif 'size' in a:
        print(len(q))
    elif 'empty' in a:
        if q:
            print(0)
        else:
            print(1)
    elif 'front' in a:
        if q:
            print(q[0])
        else:
            print(-1)
    elif 'back' in a:
        if q:
            print(q[-1])
        else:
            print(-1)