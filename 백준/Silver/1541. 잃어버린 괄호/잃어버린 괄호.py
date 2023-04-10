s = input()
lst = s.split('-')
rlt = []
for i in range(len(lst)):
    if '+' in lst[i]:
        summ=0
        tm = lst[i].split('+')
        for i in tm:
            summ += int(i)
        rlt.append(summ)
    else:
        rlt.append(int(lst[i]))

print(rlt[0]-sum(rlt[1:]))