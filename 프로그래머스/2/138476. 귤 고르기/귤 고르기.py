import collections

def solution(k, tangerine):
    answer = 0
    tan_dict = collections.Counter(tangerine)
    sort_value = sorted(tan_dict.values(), reverse=True)
    for value in sort_value:
        k -= value
        answer+=1
        if k<= 0: break
    return answer