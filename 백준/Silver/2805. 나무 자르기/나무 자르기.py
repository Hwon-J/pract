n, m = map(int, input().split())
trees = list(map(int, input().split()))

st, ed = 0, max(trees)
rlt = 0
while st <=ed:
    mid = (st+ed) // 2
    total = 0
    for tree in trees:
        if tree > mid:
            total += tree - mid
    if total < m:
        ed = mid - 1
    else:
        rlt = mid
        st = mid + 1

print(rlt)