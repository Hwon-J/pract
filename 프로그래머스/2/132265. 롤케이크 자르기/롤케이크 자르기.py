from collections import Counter

def solution(topping):
    answer = 0
    cake1 = Counter(topping)
    cake2 = {}
    for top in topping:
        if len(cake1) == len(cake2):
            answer += 1
        if top not in cake2:
            cake2[top] = 1
        else:
            cake2[top] += 1
        cake1[top] -= 1
        if cake1[top] == 0:
            del cake1[top]
    return answer