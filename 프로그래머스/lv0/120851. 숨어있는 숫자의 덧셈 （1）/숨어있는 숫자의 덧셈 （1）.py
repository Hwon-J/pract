def solution(my_string):
    lst=list(my_string)
    answer=[]
    for i in lst:
        if 48<= ord(i) <=57:
            answer.append(i)
    summ=0
    for i in answer:
        summ+=int(i)
    return summ