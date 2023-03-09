N=int(input())
lst=list(map(int, input().split()))
rlt=[-1]*N
stack=[0]
for i in range(1,N):
     while stack and lst[stack[-1]]<lst[i]:
          rlt[stack.pop()]=lst[i]
     stack.append(i)
print(*rlt)