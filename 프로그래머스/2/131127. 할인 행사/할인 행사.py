from collections import Counter
def solution(want, number, discount):
    answer = 0
    dic = dict()
    for w, n in zip(want, number):
        dic[w] = n
    for start in range(len(discount)-9):
        counter = Counter(discount[start:start+10])
        if dic == counter:
            answer += 1

    return answer