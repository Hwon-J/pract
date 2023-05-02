N, M = map(int, input().split())
person = list(map(int, input().split()))
person = person[1:]
party = [list(map(int, input().split())) for _ in range(M)]
parent = [i for i in range(N+1)]
cnt =0
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b]=a
    else:
        parent[a]=b

for i in party:
    for j in range(2,len(i)):
        union(i[1], i[j])

for i in range(len(person)):
    person[i]=find(person[i])

for i in party:
    for j in range(1,len(i)):
        if find(i[j]) in person:
            break
    else:cnt+=1
print(cnt)
