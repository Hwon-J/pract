def solution(s, n):
    answer = ''
    for i in s:
        if i.isupper():
            tm = chr((ord(i) - 65 + n) % 26 + 65)
        elif i.islower():
            tm = chr((ord(i) - 97 + n) % 26 + 97)
        else:
            tm = i
        answer += tm
    return answer
