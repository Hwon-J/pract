def solution(s):
    answer = []
    lst = s.replace('}','')
    lst = list(lst.split('{'))
    lst.sort(key=len)
    for sett in lst:
        if sett != '':
            tm = list(sett.split(','))
            for i in tm:
                if i != '':
                    if not int(i) in answer:
                        answer.append(int(i)) 
    return answer