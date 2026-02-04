# 최단 경로
# 골드 4
# 첫번째 풀이
# 간선의 가중치가 음수가 아니므로 다익스트라로 풀어도 됨
from queue import PriorityQueue
import sys
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = int(1e12)

adj_list = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj_list[u].append([v, w])


dist = [INF] * (V + 1)

pq = PriorityQueue()
pq.put([0, K])
dist[K] = 0

while not pq.empty():
    cur_dist, cur_node, = pq.get()

    # 이 문장을 없어도 맞을 수 있지만,
    # 중복탐색을 방지해주는 역할!
    # 구식경로는 없애주고, 시간초과 발생하는 것을 방지해줌
    if cur_dist > dist[cur_node]:
        continue

    for adj_node, adj_dist in adj_list[cur_node]:
        temp_dist = cur_dist + adj_dist
        if temp_dist < dist[adj_node]:
            pq.put([temp_dist, adj_node])
            dist[adj_node] = temp_dist

for v in range(1, V + 1):
    print(dist[v] if dist[v] != INF else "INF")

