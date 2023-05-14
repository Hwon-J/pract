import sys, heapq
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    min_q = []
    max_q = []
    k = int(input())
    check = [1] * k

    for i in range(k):
        cal, num = input().split()
        num = int(num)
        if cal == "I":
            heapq.heappush(min_q, (num, i))
            heapq.heappush(max_q, (-num, i))
        else:
            if num == -1:
                if min_q:
                    check[heapq.heappop(min_q)[1]] = 0
            elif num == 1:
                if min_q:
                    check[heapq.heappop(max_q)[1]] = 0

        while min_q and check[min_q[0][1]] == 0:
            heapq.heappop(min_q)
        while max_q and check[max_q[0][1]] == 0:
            heapq.heappop(max_q)

    if min_q == []:
        print("EMPTY")
    else:
        print(-max_q[0][0], min_q[0][0])
