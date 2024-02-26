from collections import deque

def solution(prices):
    answer = [0] * len(prices)
    q = deque()
    for i in range(len(prices)):
        while q and prices[i] < prices[q[-1]]:
            j = q.pop()
            answer[j] = i - j
        q.append(i)

    while q:
        j = q.pop()
        answer[j] = len(prices) - 1 - j

    return answer
