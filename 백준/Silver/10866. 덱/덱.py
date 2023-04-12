from collections import deque
import sys
input = sys.stdin.readline
q= deque()
N = int(input())
for _ in range(N):
    a = input()
    if 'push_back' in a:
        tm = list(a.split())
        q.append(tm[1])
    elif 'push_front' in a:
        tm = list(a.split())
        q.appendleft(tm[1])
    elif 'pop' in a:
        if q:
            if 'front' in a:
                print(q.popleft())
            else:
                print(q.pop())
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