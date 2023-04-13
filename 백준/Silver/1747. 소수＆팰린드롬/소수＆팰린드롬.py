N = int(input())
m = 1005000
arr = [True]*(m)
arr[0],arr[1]=False,False


for i in range(2, m):
    if not arr[i]:continue
    j=2
    while i*j<m:
        arr[i*j]=False
        j+=1

while 1:
    if arr[N]:
        tm = str(N)
        if tm ==tm[::-1]:
            print(int(tm))
            break
    N+=1