def solution(sides):
    lst=sorted(sides)
    if lst[2]>=lst[0]+lst[1]:
        return 2
    else:
        return 1