def solution(array):
    ans=[]
    maxx=0
    for i in array:
        if i>maxx:
            maxx=i
    ans.append(maxx)
    idx=array.index(maxx)
    ans.append(idx)
    return ans