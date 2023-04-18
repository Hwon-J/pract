import math
mn, mx = map(int, input().split())
arr=[False]*(mx-mn+1)

so = int(mx**0.5)+1
lst = [i**2 for i in range(2,so)]

for i in lst:
    tm = (math.ceil(mn/i)*i)-mn
    while tm <=mx-mn:
        arr[tm]=True
        tm+=i
print(arr.count(False))