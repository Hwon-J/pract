N = int(input())
for _ in range(N):
    lst = list(input())
    summ=0
    tm = 0
    for i in lst:
        if i=='O':
            tm+=1
            summ+=tm
        else:
            tm =0
    print(summ)