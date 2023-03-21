import sys
input = sys.stdin.readline
N=int(input())
Bucket=[0]*10001
for i in range(N):
    Bucket[int(input())]+=1
tm=0
while tm<10001:
    if Bucket[tm]!=0:
        while Bucket[tm]>0:
            print(tm)
            Bucket[tm]-=1
        tm+=1
    else:
        tm+=1