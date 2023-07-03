n = int(input())
tm = n//2
summ = 0
if n%2==0:
    summ=(1+n)*tm
else:
    summ=(1+n)*tm + tm+1
print(summ)