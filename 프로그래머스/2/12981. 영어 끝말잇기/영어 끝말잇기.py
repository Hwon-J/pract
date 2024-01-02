def solution(n, words):
    answer = []
    tm = []
    cnt = 1
    for word in words:
        if word in tm:
            break
        else:
            if not tm or tm[-1][-1] == word[0]:
                tm.append(word)
                cnt+=1
            else:
                break
    if cnt > len(words):
        answer = [0,0]
    else:
        if cnt % n == 0:
            answer.append(n)
            answer.append(cnt // n)
        else:
            answer.append((cnt % n))
            answer.append((cnt // n) + 1)
    return answer