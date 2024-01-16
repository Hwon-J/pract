from collections import Counter

def solution(str1, str2):
    answer = 1
    setA = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            setA.append(str1[i:i+2].lower())
    setB = []
    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            setB.append(str2[i:i+2].lower())
    
    if len(setA)==0 and len(setB)==0:
        return 65536
    else:
        cntA = Counter(setA)
        cntB = Counter(setB)
        intersec = cntA & cntB
        union = cntA | cntB
        answer = int(sum(intersec.values()) / sum(union.values()) * 65536)
        return answer