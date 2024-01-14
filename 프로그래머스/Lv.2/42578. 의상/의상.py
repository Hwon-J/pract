def solution(clothes):
    answer = 1
    cloth_cnt = {}
    for cloth in clothes:
        if cloth[1] in cloth_cnt:
            cloth_cnt[cloth[1]] += 1
        else:
            cloth_cnt[cloth[1]] = 1
    for value in cloth_cnt.values():
        answer *= value+1
    return answer - 1