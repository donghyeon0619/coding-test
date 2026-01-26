# 바이러스
# 첫번쨰 풀이
# bfs를 활용해서 문제를 품
import sys
input = sys.stdin.readline
from collections import deque

def bfs(node):
    global adj_list, visited, cnt

    q = deque()
    q.append(node)
    visited[node] = True

    while q:
        v = q.popleft()

        for adj_node in adj_list[v]:
            if not visited[adj_node]:
                q.append(adj_node)
                visited[adj_node] = True
                cnt += 1


N = int(input())
E = int(input())

adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(E):

    s, e = map(int, input().split())

    adj_list[s].append(e)
    adj_list[e].append(s)

cnt = 0

bfs(1)
print(cnt)

## 두번째 풀이
## dfs를 이용해서 문제를 품

import sys
input = sys.stdin.readline

def dfs(node):
    global adj_list, visited, cnt

    if visited[node]:
        return

    visited[node] = True
    cnt += 1

    for v in adj_list[node]:
        dfs(v)


N = int(input())
E = int(input())

adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(E):

    s, e = map(int, input().split())

    adj_list[s].append(e)
    adj_list[e].append(s)

cnt = 0

dfs(1)
print(cnt - 1)


## 세번째 풀이
## deque를 사용하지 않고 직접 구현
import sys
input = sys.stdin.readline

def bfs(v):
    global visited, adj_list, cnt

    q = [v]
    visited[v] = True

    while q:
        s = q.pop(0)

        for adj_node in adj_list[s]:
            if not visited[adj_node]:
                q.append(adj_node)
                visited[adj_node] = True
                cnt += 1


N = int(input())
E = int(input())

adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(E):

    s, e = map(int, input().split())

    adj_list[s].append(e)
    adj_list[e].append(s)

cnt = 0

bfs(1)
print(cnt)

