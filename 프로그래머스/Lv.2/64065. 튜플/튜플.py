def solution(s):
    answer = []
    lst = s[2:-2].split('},{')
    lst.sort(key=len)
    for sett in lst:
        tm = list(map(int,sett.split(',')))
        for i in tm:
            if not i in answer:
                answer.append(i) 
    return answer