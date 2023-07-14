from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    q = deque(people)

    while q:
        tm = q.pop()
        answer += 1

        while q:
            if tm + q[0] <= limit:
                tm += q.popleft()
            else:
                break

    return answer
