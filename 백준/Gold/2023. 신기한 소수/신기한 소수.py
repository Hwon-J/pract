N=int(input())
st=[2,3,5,7]

def sosu(num):
    for j in range(2, (num//2)+1):
        if num % j == 0:
            return 0
    return 1


def ans(tm):
    if len(str(tm))==N:
        print(tm)
    else:
        for i in (1,3,5,7,9):
            temp = tm*10 + i
            if sosu(temp)==1:
                ans(temp)


for i in st:
    ans(i)