def solution(hp):
    j=hp//5
    b=(hp-(j*5))//3
    i=(hp-(j*5+b*3))//1
    return j+b+i