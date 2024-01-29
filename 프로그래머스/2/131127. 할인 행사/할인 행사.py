def matching(dc, want, number):
    for i in range(len(want)):
        if dc[want[i]] != number[i]:
            return 0
    return 1

from collections import Counter

def solution(want, number, discount):
    answer = 0
    for i in range(len(discount)-10+1):
        DC = Counter(discount[i:10+i])
        answer += matching(DC, want, number)
    return answer