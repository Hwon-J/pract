N = int(input())
for _ in range(N):
    flag =1
    stack = []
    lst = list(input())
    for i in lst:
        if i=='(':
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                flag = 0
                print('NO')
                break
    if flag==1 and not stack:
        print('YES')
    elif stack:
        print('NO')