def solution(s):
    answer = ''
    words = s.lower().split(' ')
    for i in range(len(words)):
        if words[i] and ord(words[i][0]) >= 97:
            words[i] = chr(ord(words[i][0]) - 32) + words[i][1:]
    answer = " ".join(words)
    return answer
