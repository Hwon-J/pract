k, n = map(int, input().split())
lst = [int(input()) for _ in range(k)]

st, ed = 1, max(lst)
while st <= ed:
    mid = (st+ed) // 2
    cnt = 0
    for i in lst:
        cnt += i // mid
    if cnt < n:
        ed = mid - 1
    else:
        st = mid + 1

print(ed)