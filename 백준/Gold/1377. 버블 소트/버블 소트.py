import sys
input=sys.stdin.readline
N= int(input())
lst=[]
for i in range(N):
    tm=int(input())
    lst.append((int(tm),i))
arr=sorted(lst)
mx=0
for i in range(N):
    if mx< arr[i][1]-i+1:
        mx=arr[i][1]-i+1

print(mx)