# N: 강의의 수, M : 블루레이 수
N, M = map(int, input().split())
lst = list(map(int, input().split()))
st,ed = max(lst),sum(lst)
while 1:
    mid = (st+ed)//2
    cnt,summ=1,0
    for i in lst:
        if summ + i > mid:
            cnt+=1
            summ=0
        summ+=i
    if cnt > M:
        st = mid+1
    else:
        ed=mid-1

    if st>ed:
        break
print(st)