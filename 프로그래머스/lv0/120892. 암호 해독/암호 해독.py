def solution(cipher, code):
    lst=list(cipher)
    real=[]
    for i in range(code-1,len(lst),code):
        real.append(lst[i])
    str=''.join(real)
    return str