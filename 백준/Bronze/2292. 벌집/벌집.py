N = int(input())
cnt =1
N-=1
tm = 1
while N>0:
    N = N-(6*tm)
    tm+=1
    cnt+=1
print(cnt)