
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
def check(s):
    while True:
        if '()' not in s and '[]' not in s and '{}' not in s:
            break
        s = s.replace('()', '')
        s = s.replace('[]', '')
        s = s.replace('{}', '')
    return 1 if len(s) == 0 else 0

def solution(s):
    answer = 0

    for i in range(len(s)):
        answer += check(s)
        s = s[1:] + s[0]

    return answer