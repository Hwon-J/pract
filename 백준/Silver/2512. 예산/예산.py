n = int(input())
budgets = list(map(int, input().split()))
m = int(input())

st, ed = 0, max(budgets)
while st <= ed:
    mid = (st + ed) // 2
    tm = 0
    for i in budgets:
        if i >= mid:
            tm += mid
        else:
            tm += i
    if tm <= m:
        st = mid + 1
    else:
        ed = mid - 1
print(ed)