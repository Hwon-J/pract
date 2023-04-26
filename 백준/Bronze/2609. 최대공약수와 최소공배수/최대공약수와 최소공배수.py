a,b = map(int, input().split())
m, n = a,b
while n != 0:
    m, n = n, m % n

print(m)

tm = 0
for i in range(a,0,-1):
    if a%i==0 and b%i==0:
        tm = i
        break

print(a*b//tm)