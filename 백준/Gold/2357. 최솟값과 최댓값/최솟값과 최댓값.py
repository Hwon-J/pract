import sys
input = sys.stdin.readline

def make_tree(lst, tree, node, st, ed):
    if st == ed:
        tree[node] = (lst[st], lst[st])
    else:
        mid = (st + ed) // 2
        make_tree(lst, tree, 2*node, st, mid)
        make_tree(lst, tree, 2*node + 1, mid + 1, ed)
        tree[node] = (min(tree[2*node][0], tree[2*node + 1][0]), max(tree[2*node][1], tree[2*node + 1][1]))

def calculate(tree, node, st, ed, left, right):
    if right < st or left > ed:
        return float('inf'), -float('inf')
    if left <= st and right >= ed:
        return tree[node]
    mid = (st + ed) // 2
    min_left, max_left = calculate(tree, 2*node, st, mid, left, right)
    min_right, max_right = calculate(tree, 2*node + 1, mid + 1, ed, left, right)
    return min(min_left, min_right), max(max_left, max_right)

N, M = map(int, input().split())
lst = [int(input()) for _ in range(N)]

tree_size = 1
while tree_size < N:
    tree_size *= 2
tree = [(float('inf'), -float('inf'))] * (2 * tree_size)
make_tree(lst, tree, 1, 0, N - 1)

for _ in range(M):
    a, b = map(int, input().split())
    mn, mx = calculate(tree, 1, 0, N - 1, a - 1, b - 1)
    print(mn, mx)
