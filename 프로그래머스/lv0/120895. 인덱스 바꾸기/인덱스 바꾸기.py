def solution(my_string, num1, num2):
    st=list(map(str, my_string))
    st[num1],st[num2]= st[num2],st[num1]
    rlt=''.join(st)
    return rlt