def solution(k, tangerine):
    answer = 0
    tan_dict = {}
    for size in tangerine:
        if size in tan_dict:
            tan_dict[size] += 1
        else:
            tan_dict[size] = 1
    sort_value = sorted(tan_dict.values(), reverse=True)
    for value in sort_value:
        k -= value
        answer+=1
        if k<= 0: break
    return answer