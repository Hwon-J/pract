def solution(s):
    answer = ''
    tm = list(s)
    tm .sort(reverse=True)
    answer = ''.join(tm)
    return answer