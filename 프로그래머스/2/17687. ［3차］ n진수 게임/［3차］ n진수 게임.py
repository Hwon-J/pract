def formation(number, base):
    if number == 0:
        return '0'
    else:
        result = ''
        while number > 0:
            remain = number % base
            if remain >= 10:
                result = chr(ord('A') + remain - 10) + result
            else:
                result = str(remain) + result
            number //= base
        return result

def solution(n, t, m, p):
    answer = ''
    ed = t * m
    number = 0
    
    while ed > 0:
        tm = formation(number, n)
        answer += tm
        ed -= len(tm)
        number += 1

    answer = answer[p - 1::m][:t]
    
    return answer