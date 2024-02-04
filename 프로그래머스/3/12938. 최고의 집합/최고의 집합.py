def solution(n, s):
    answer = []
    if s < n:
        answer = [-1]
        return answer
    quot = s // n
    remain = s % n
    for i in range(n-remain):
        answer.append(quot)
    for i in range(remain):
        answer.append(quot+1)
    return answer