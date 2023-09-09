def solution(s):
    answer = ''
    tm = 1
    for i in s:
        if i != ' ':
            if tm % 2 == 1:
                answer += i.upper()
                tm+=1
            else:
                answer += i.lower()
                tm+=1
        else:
            answer += ' '
            tm = 1
    return answer