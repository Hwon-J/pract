import sys
input = sys.stdin.readline

N = int(input())
Nlist = list(map(int, input().split()))
M = int(input())
Mlist = list(map(int, input().split()))
Nlist.sort()

def Find(st, ed, num):
    while 1:
        mid = (st+ed)//2
        if Nlist[mid] == num:
            return 1
        elif Nlist[mid] > num:
            ed = mid-1
        elif Nlist[mid] < num:
            st = mid+1
        if st>ed:
            return 0

for i in range(M):
    rlt =Find(0,N-1,Mlist[i])
    print(rlt)