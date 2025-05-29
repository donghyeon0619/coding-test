## 백준 실버 2
## DFS와 BFS
## 첫번째 풀이
## 정석풀이
## 입력이 조건에서 "양방향"으로 주어졌으므로 인접리스트에 양쪽 노드에 대해 연결된 노드 추가해야 함
import sys
from collections import deque
input = sys.stdin.readline


# dfs 함수 정의
def dfs(node):

    global dfs_visited, adj_list

    # base case
    if dfs_visited[node]:
        return
    dfs_visited[node] = True

    print(node, end=' ')

    # recursive case
    for adj_node in adj_list[node]:
        dfs(adj_node)


# bfs 함수 정의
def bfs(node):
    global bfs_visited, adj_list
    q = deque()

    q.append(node)
    bfs_visited[node] = True
    while q:
        node = q.popleft()
        print(node, end=' ')

        for adj_node in adj_list[node]:
            if bfs_visited[adj_node]:
                continue

            q.append(adj_node)
            bfs_visited[adj_node] = True


N, M, V = map(int, input().split())

dfs_visited = [False] * (N + 1)
bfs_visited = [False] * (N + 1)
adj_list = [[] for _ in range(N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    adj_list[s].append(e)
    adj_list[e].append(s)

for i in range(1, N + 1):
    if len(adj_list[i]) > 1:
        adj_list[i].sort()

dfs(V)
print()
bfs(V)


## 두번째 풀이
## visted 상태 저장 변수를 하나로만 하고, base_case도 for문 내부에서 조건문으로 설정해서 품
## deque모듈 사용 없이 기존의 리스트에서 큐를 구현
import sys
input = sys.stdin.readline


def dfs(v):
    # 재귀
    visited[v] = True
    ans_dfs.append(v)

    for i in graph[v]:
        if not visited[i]:
            dfs(i)


def bfs(v):
    q = [v]
    ans_bfs.append(v)
    visited[v] = True
    while q:
        s = q.pop(0)

        for i in graph[s]:
            if not visited[i]:
                q.append(i)
                ans_bfs.append(i)
                visited[i] = True


N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(N+1):
    graph[i].sort()

visited = [False] * (N+1)
ans_dfs = []
dfs(V)

visited = [False] * (N+1)
ans_bfs = []
bfs(V)

print(*ans_dfs)
print(*ans_bfs)


