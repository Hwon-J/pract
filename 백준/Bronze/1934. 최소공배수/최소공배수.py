T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    tm = 0
    for i in range(a,0,-1):
        if a%i==0 and b%i==0:
            tm = i
            break

    print(a*b//tm)