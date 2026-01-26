## BOJ 1260
from collections import deque
import sys
input = sys.stdin.readline

def dfs(node):
    global adj_list, dfs_visited

    if dfs_visited[node]:
        return
    dfs_visited[node] = True

    print(node, end=" ")

    for v in adj_list[node]:
        dfs(v)


def bfs(node):
    global adj_list, bfs_visited

    q = deque([node])
    bfs_visited[node] = True

    while q:
        v = q.popleft()
        print(v, end=" ")

        for a_v in adj_list[v]:
            if not bfs_visited[a_v]:
                bfs_visited[a_v] = True
                q.append(a_v)


N, M, V = map(int, input().split())
adj_list = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

for n in range(N + 1):
    adj_list[n].sort()

dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)


dfs(V)
print()
bfs(V)







