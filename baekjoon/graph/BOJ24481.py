# 깊이 우선 탐색 3
# 실버 2
# 재귀를 이용한 풀이
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

def dfs(node, depth):

    global graph, visited

    if visited[node] != -1:
        return
    visited[node] = depth

    if len(graph[node]) > 1:
        graph[node].sort()

    for adj_node in graph[node]:
        dfs(adj_node, depth + 1)


N, M, R, = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [-1] * (N + 1)


for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


dfs(R, 0)

for i in range(1, N+1):
    print(visited[i])


# 두번쨰 풀이
# 스택을 이용한 풀이
import sys

input = sys.stdin.readline

N, M, R, = map(int, input().split())


def dfs(start):
    stack = [(start, 0)]
    while stack:
        node, depth = stack.pop()

        if visited[node] != -1:
            continue

        visited[node] = depth

        if len(graph[node]) > 1:
            graph[node].sort()

        for next_node in reversed(graph[node]):
            if visited[next_node] == -1:
                stack.append((next_node, depth + 1))


graph = [[] for _ in range(N+1)]
visited = [-1] * (N + 1)


for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

dfs(R)

for i in range(1, N+1):
    print(visited[i])




