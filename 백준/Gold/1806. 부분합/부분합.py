N, S = map(int, input().split())
lst = list(map(int, input().split()))

min_cnt = N + 1
summ = lst[0]
st, ed = 0, 0
while st < N and ed < N:  
    if summ < S:
        ed += 1
        if ed == N: 
            break
        summ += lst[ed]
    else:
        min_cnt = min(min_cnt, ed - st + 1)
        summ -= lst[st]
        st += 1

if min_cnt == N + 1:
    print(0)
else:
    print(min_cnt)
