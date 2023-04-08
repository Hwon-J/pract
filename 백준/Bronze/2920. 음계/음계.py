lst = list(map(int, input().split()))
ans = [1,2,3,4,5,6,7,8]
if lst == ans:
    print('ascending')
elif lst == ans[::-1]:
    print('descending')
else:
    print('mixed')