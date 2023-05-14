import sys, heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    min_q = []
    max_q = []
    k = int(input())
    check = [0] * k

    for i in range(k):
        a, b = input().split()
        if a == "I":
            heapq.heappush(min_q, (int(b), i))
            heapq.heappush(max_q, (-int(b), i))
        else:
            if b == '1':
                if min_q:
                    check[heapq.heappop(max_q)[1]] = 1
            else:
                if min_q:
                    check[heapq.heappop(min_q)[1]] = 1

        while min_q and check[min_q[0][1]] == 1:
            heapq.heappop(min_q)
        while max_q and check[max_q[0][1]] == 1:
            heapq.heappop(max_q)

    if not min_q:
        print("EMPTY")
    else:
        mx = heapq.heappop(max_q)
        mn = heapq.heappop(min_q)
        print(-mx[0], mn[0])
