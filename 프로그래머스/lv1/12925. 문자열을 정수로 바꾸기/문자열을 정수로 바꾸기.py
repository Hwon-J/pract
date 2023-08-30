def solution(s):
    answer = 0
    if s[0]!='-':
        answer = int(s)
    else:
        answer = -int(s[1:])
    return answer