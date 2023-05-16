from collections import deque

N, K = map(int, input().split())

lst = []
arr = deque(range(1, N + 1))

while arr:
    for _ in range(K - 1):
        arr.append(arr.popleft())
    lst.append(arr.popleft())

output_str = '<' + ', '.join(map(str, lst)) + '>'
print(output_str)