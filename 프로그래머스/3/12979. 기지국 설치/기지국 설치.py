def solution(n, arr, w):
    bef=-w
    cnt=0
    ww=w*2+1
    for x in arr:
        cnt+=(x-bef-1)//ww
        bef=x
    return cnt+(n+w-bef)//ww
