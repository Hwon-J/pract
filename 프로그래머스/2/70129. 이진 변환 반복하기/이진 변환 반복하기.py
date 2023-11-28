def solution(s):
    answer = []
    cnt = 0
    zero = 0
    while 1:
        if s == "1":
            break
        tm = s.count("1")
        zero += s.count("0")
        s = format(tm, 'b')
        cnt +=1
    answer.append(cnt)
    answer.append(zero)
    return answer