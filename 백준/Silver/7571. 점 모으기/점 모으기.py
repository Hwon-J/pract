N,M=map(int, input().split())
x=[]
y=[]
for p in range(M):
     i,j=map(int, input().split())
     x.append(i)
     y.append(j)
x.sort()
y.sort()
q,w=x[M//2],y[M//2]
summ=0
for i in range(M):
     summ+=(abs(q-x[i])+abs(w-y[i]))
print(summ)