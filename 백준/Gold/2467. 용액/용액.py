N = int(input())
lst = list(map(int, input().split()))
answer = [0, 0]
st, ed = 0, N-1
mn = int(21e8)

while st < ed:
    tm = lst[st] + lst[ed]
    if abs(tm) < mn:
        mn = abs(tm) 
        answer[0], answer[1] = lst[st], lst[ed]
    if tm == 0:
        break 
    elif tm < 0:
        st += 1
    else:
        ed -= 1

print(answer[0], answer[1])
