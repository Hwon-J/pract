N = int(input())
rlt = 1
cnt = 0

while N>0:
    rlt *=N
    N-=1

res = list(str(rlt))
for i in range(len(res)-1,-1,-1):
    if res[i]=='0':
        cnt+=1
    else:
        break
print(cnt)