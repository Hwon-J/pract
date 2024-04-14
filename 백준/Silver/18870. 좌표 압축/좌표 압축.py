n = int(input())
lst = list(map(int, input().split()))
sort_lst = sorted(set(lst))
index_dict = {sort_lst[i]: i for i in range(len(sort_lst))}
for num in lst:
    print(index_dict[num], end=' ')