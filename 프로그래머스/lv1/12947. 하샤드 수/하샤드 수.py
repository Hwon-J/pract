def solution(x):
    answer = False
    tm = sum(map(int, str(x)))
    if x % tm == 0:
        answer = True
    return answer