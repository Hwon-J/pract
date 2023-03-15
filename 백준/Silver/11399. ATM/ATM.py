N=int(input())
lst=list(map(int, input().split()))
lst.sort()
rlt=lst[0]
summ=lst[0]
for i in range(1,N):
    summ+=lst[i]
    rlt+=summ
print(rlt)
