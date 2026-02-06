# 특정한 최단 경로
# 골드 4
# dist[]라는 개념적 의미에 대해서 생각해볼 수 있는 문제
# dist[]를 하나 만들라는 법이 없음.
# 그리고 dist[]는 어떤점에 시작헀을때 어떤 점까지의 최단경로를 저장하는 것이므로 여러개 일 수도 있음
import sys
from queue import PriorityQueue

input = sys.stdin.readline

def dijkstra(s, dist):
    global adj_list

    pq = PriorityQueue()
    pq.put([0, s])
    dist[s] = 0

    while not pq.empty():
        cur_dist, cur_node = pq.get()

        if cur_dist > dist[cur_node]:
            continue

        for adj_node, adj_dist in adj_list[cur_node]:
            temp_dist = cur_dist + adj_dist
            if temp_dist < dist[adj_node]:
                pq.put([temp_dist, adj_node])
                dist[adj_node] = temp_dist


INF = int(1e12)

N, E = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
for e in range(E):
    a, b, c = map(int, input().split())
    adj_list[a].append([b, c])
    adj_list[b].append([a, c])

v1, v2 = map(int, input().split())

dist_1 = [INF for _ in range(N + 1)]
dist_v1 = [INF for _ in range(N + 1)]
dist_v2 = [INF for _ in range(N + 1)]

dijkstra(1, dist_1)
dijkstra(v1, dist_v1)
dijkstra(v2, dist_v2)


shortest_dist1 = dist_1[v1] + dist_v1[v2] + dist_v2[N]
if dist_1[v1] == INF or dist_v1[v2] == INF or dist_v2[N] == INF:
    shortest_dist1 = INF

shortest_dist2 = dist_1[v2] + dist_v2[v1] + dist_v1[N]
if dist_1[v2] == INF or dist_v2[v1] == INF or dist_v1[N] == INF:
    shortest_dist2 = INF

ans = -1

if shortest_dist1 != INF and shortest_dist2 != INF:
    if shortest_dist1 > shortest_dist2:
        ans = shortest_dist2
    else:
        ans = shortest_dist1

elif shortest_dist1 != INF:
    ans = shortest_dist1
elif shortest_dist2 != INF:
    ans = shortest_dist2

print(ans)

# 두번째 풀이
# 처음 풀이해서 똑같이 반복되는 부분을 함수로 빼고 좀더 간략하게
# 가독성 있게 바뀐 코드

import sys
from queue import PriorityQueue

input = sys.stdin.readline

def dijkstra(s, dist):
    global adj_list

    pq = PriorityQueue()
    pq.put([0, s])
    dist[s] = 0

    while not pq.empty():
        cur_dist, cur_node = pq.get()

        if cur_dist > dist[cur_node]:
            continue

        for adj_node, adj_dist in adj_list[cur_node]:
            temp_dist = cur_dist + adj_dist
            if temp_dist < dist[adj_node]:
                pq.put([temp_dist, adj_node])
                dist[adj_node] = temp_dist


def path_costs(*dists):
    # dists 중 하나라도 INF면 INF 반환, 아니면 합
    total = 0
    for d in dists:
        if d == INF:
            return INF
        total += d
    return total


INF = int(1e12)

N, E = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
for e in range(E):
    a, b, c = map(int, input().split())
    adj_list[a].append([b, c])
    adj_list[b].append([a, c])

v1, v2 = map(int, input().split())

dist_1 = [INF for _ in range(N + 1)]
dist_v1 = [INF for _ in range(N + 1)]
dist_v2 = [INF for _ in range(N + 1)]

dijkstra(1, dist_1)
dijkstra(v1, dist_v1)
dijkstra(v2, dist_v2)

route1 = path_costs(dist_1[v1], dist_v1[v2], dist_v2[N])
route2 = path_costs(dist_1[v2], dist_v2[v1], dist_v1[N])

ans = min(route1, route2)
print(-1 if ans == INF else ans)
