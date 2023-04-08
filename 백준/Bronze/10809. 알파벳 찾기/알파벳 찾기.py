a = list(input())
bucket = [-1]*26
for i in range(len(a)):
    if bucket[ord(a[i])-ord('a')] == -1:
        bucket[ord(a[i]) - ord('a')] = i
print(*bucket)