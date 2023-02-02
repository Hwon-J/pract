def solution(age):
    age1=list(map(int,str(age)))
    rlt=[]
    for i in age1:
        for j in range(10):
            if i==j:
                rlt.append(chr(97+j))
    result=''.join(rlt)
    return result