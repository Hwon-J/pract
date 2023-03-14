N=list(input())
N.sort(key=int)
rlt=N[::-1]
print(''.join(rlt))