def solution(s):
    answer = ''
    tm = len(s)//2
    if len(s)%2==1:
        answer = s[tm]
    else:
        answer = s[tm-1:tm+1]
    return answer