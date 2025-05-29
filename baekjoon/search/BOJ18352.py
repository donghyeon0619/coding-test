# 특정 거리의 도시 찾기
# 실버 2
# 첫번쨰 풀이
# 일반적인 BFS 풀이
import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, k):

    q = deque()
    q.append((0, x))
    visited[x] = True

    while q:
        distance, node = q.popleft()

        if distance == k:
            city.append(node)
            continue

        for adj_node in adj_list[node]:
            if visited[adj_node]:
                continue

            q.append((distance + 1, adj_node))
            visited[adj_node] = True


N, M, K, X = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
city = []

for _ in range(M):
    a, b = map(int, input().split())
    adj_list[a].append(b)

bfs(X, K)

if len(city) == 0:
    print(-1)
else:
    city.sort()
    print(*city, sep="\n")

## 두번쨰 풀이
## 튜플 언패킹을 사용하지 않고 정수 한개만 큐에 넣기/빼기 -> 메모리 cpu 오버헤드 최소화
## 지역바인딩을 통해서 전역 조회비용 절감
## 정답 수집 후 정렬 대신 1~N 순회만 해서 자동으로 오름차순
# import sys
# from collections import deque
# input = sys.stdin.readline
#
#
# def bfs(n, k, x, adj):
#
#     dist = [-1] * (n+1)
#     dist[x] = 0
#     q = deque([x])
#
#     local_adj = adj
#     local_dist = dist
#     pop, append = q.popleft, q.append
#
#     while q:
#         v = pop()
#         d = local_dist[v]
#
#         if d == k:
#             continue
#
#         for w in local_adj[v]:
#             if local_dist[w] == -1:
#                 local_dist[w] = d + 1
#                 append(w)
#
#     return dist
#
#
# N, M, K, X = map(int, input().split())
# adj_list = [[] for _ in range(N+1)]
# for _ in range(M):
#     a, b = map(int, input().split())
#     adj_list[a].append(b)
#
#
# dist = bfs(N, K, X, adj_list)
#
# found = False
# out = []
# for i in range(1, N+1):
#     if dist[i] == K:
#         out.append(str(i))
#         found = True
#
# if not found:
#     print(-1)
# else:
#     print("\n".join(out))

## 세번쨰 풀이
## 다익스트라를 이용한 풀이
## heapq를 이용함
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 10^9으로 큰값을 고정시키려고 넣은 것

N, M, K, X = map(int, input().split())
graph = [[] for _ in range(N + 1)]
distance = [INF] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append((b, 1))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for j in graph[now]:
            cost = dist + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost
                heapq.heappush(q, (cost, j[0]))

dijkstra(X)
answer = []
for i in range(1, N+1):
    if distance[i] == K:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)


