def solution(array, height):
    lst=[]
    for i in array:
        if i>height:
            lst.append(i)
    return len(lst)