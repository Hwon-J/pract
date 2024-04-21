import sys
input = sys.stdin.readline

n = int(input())
tops = list(map(int, input().split()))
answer = [0]*(n+1)
stack = []

for i in range(1, n+1):
    while stack:
        if tops[i-1] > stack[-1][0]:
            stack.pop()
        else:
            answer[i] = stack[-1][1]
            break
    stack.append((tops[i-1],i))
print(*answer[1:])