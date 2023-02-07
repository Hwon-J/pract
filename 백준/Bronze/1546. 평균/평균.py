n=int(input())
lst=list(map(int, input().split()))
maxx=0
new=[]
for i in lst:
    if i>maxx:
        maxx=i
for i in lst:
    new.append(i/maxx*100)
summ=0
for i in new:
    summ+=i
print(summ/n)