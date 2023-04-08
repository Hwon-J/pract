total = 1
for _ in range(3):
    a = int(input())
    total *= a
total = list(str(total))
for i in range(10):
    print(total.count(str(i)))