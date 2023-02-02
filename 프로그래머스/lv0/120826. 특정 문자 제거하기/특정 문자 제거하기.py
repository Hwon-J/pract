def solution(my_string, letter):
    lst=list(my_string)
    new=[]
    for i in lst:
        if i!= letter:
            new.append(i)
    rlt=''.join(new)
    return rlt