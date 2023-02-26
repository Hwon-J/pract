G,S=map(int, input().split())
N=int(input())
garo=[0]
sero=[0]
for i in range(N):
    a,b=map(int,(input().split()))
    if a==0:
        sero.append(b)
    else:
        garo.append(b)
garo.append(G)
sero.append(S)
garo.sort()
sero.sort()
gmx=0
for j in range(len(garo)-1):
    if gmx <abs(garo[j]-garo[j+1]):
        gmx=abs(garo[j]-garo[j+1])
smx=0
for k in range(len(sero)-1):
    if smx < abs(sero[k]-sero[k+1]):
        smx = abs(sero[k] - sero[k + 1])
print(gmx*smx)