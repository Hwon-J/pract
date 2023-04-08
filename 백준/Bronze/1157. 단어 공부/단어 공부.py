word = input().upper()
lst = list(set(word))
cnt =[]

for i in lst :
    tm = word.count(i)
    cnt.append(tm)

if cnt.count(max(cnt)) != 1:
    print('?')
else:
    tm = cnt.index(max(cnt))
    print(lst[tm])