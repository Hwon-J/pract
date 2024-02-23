from collections import deque
T = int(input())
for _ in range(T):
    func = input()
    num = int(input())
    lst = input()[1:-1].split(',')
    if num == 0:
        q = deque()
    else:
        q = deque(lst)
    rev = False
    err = False
    for i in func:
        if i == 'R':
            rev = not rev
        else:
            if not q:
                err = True
                break
            if rev:
                q.pop()
            else:
                q.popleft()
    if err:
        print('error')
    else:
        if rev:
            q.reverse()
        print('[' + ','.join(q) + ']')