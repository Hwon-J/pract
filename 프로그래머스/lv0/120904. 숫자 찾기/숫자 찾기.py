def solution(num, k):
    st=list(map(int,str(num)))
    for i in range(len(st)):
        if st[i]==k:
            return i+1
            break
    else:
        return -1