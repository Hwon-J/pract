N = int(input())
lst = list(map(int, input().split()))
rlt =[0]*(N)

for i in range(N):
    cnt = 0
    for j in range(N):
        if lst[i]==cnt and rlt[j]==0:
            rlt[j]=i+1
            break
        if rlt[j]==0:
            cnt+=1
print(*rlt)