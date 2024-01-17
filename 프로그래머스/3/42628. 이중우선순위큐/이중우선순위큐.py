import heapq

def solution(operations):
    answer = []
    min_q = [] 
    max_q = []
    check = [0] * len(operations)

    for i in range(len(operations)):
        if operations[i][0] == "I":
            num = int(operations[i][2:])
            heapq.heappush(min_q, [num, i])
            heapq.heappush(max_q, [-num, i])
        else:
            if operations[i][2] == "-":
                while min_q and check[min_q[0][1]] == 1:
                    heapq.heappop(min_q)
                if min_q:
                    check[min_q[0][1]] = 1
                    heapq.heappop(min_q)
            else:
                while max_q and check[max_q[0][1]] == 1:
                    heapq.heappop(max_q)
                if max_q:
                    check[max_q[0][1]] = 1
                    heapq.heappop(max_q)

    while min_q and check[min_q[0][1]] == 1:
        heapq.heappop(min_q)
    while max_q and check[max_q[0][1]] == 1:
        heapq.heappop(max_q)

    if not min_q:
        answer = [0, 0]
    else:
        answer = [-max_q[0][0], min_q[0][0]]

    return answer