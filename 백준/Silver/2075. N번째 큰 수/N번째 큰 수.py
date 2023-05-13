import sys
input = sys.stdin.readline
q=[]
N = int(input())
for _ in range(N):
    arr = list(map(int, input().split()))
    q = q+arr
    q.sort()
    q=q[-N:]
print(q[0])
