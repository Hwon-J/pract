from collections import Counter
def solution(gems):
    answer = [0, len(gems)-1]
    gem_cnt = len(Counter(gems))
    st, ed = 0,0
    mn = len(gems)+1
    gem_dict = {}
    
    while ed < len(gems):
        if gems[ed] not in gem_dict:
            gem_dict[gems[ed]] = 1
        else:
            gem_dict[gems[ed]] += 1
        while len(gem_dict) == gem_cnt:
            if ed - st < mn:
                mn = ed - st
                answer = [st, ed]
            gem_dict[gems[st]] -= 1
            if gem_dict[gems[st]] == 0:
                del gem_dict[gems[st]]
            st += 1
        ed += 1
    return [answer[0]+1, answer[1]+1]