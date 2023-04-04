import sys
input = sys.stdin.readline
# N: 동전 종류, K: 필요한 돈
N, K = map(int, input().split())
# 동전 리스트 만들기
coin=[]
for i in range(N):
    a = int(input())
    coin.append(a)
coin.sort(reverse=True)
cnt=0
while K>0:
    for i in range(N):
        if K//coin[i]!=0:
            cnt+=(K//coin[i])
            K = (K % coin[i])
print(cnt)