# 다익스트라 알고리즘
# 정의
# 한 노드에서 다른 모든 노드까지의 최단 경로/거리를 구하는 알고리즘
#
# 특징
#   - 음수 간선이 존재하지 않을때만 사용할 수 있다.
#   - 시작(기준) 노드로부터 가까운 노드를 "그리디"하게 방문한다.
#
# 로직
#   - 현재 살펴보지 않은 경로 중에서 "가장 거리가 짧은" 경로를 먼저 살펴봄
#   - 경로들을 Heap(priority queue)자료형에 담고 짧은 경로부터 꺼내서 탐색
#
# 코드
from queue import PriorityQueue

INF = int(1e12)
N = 5

adj_list = [[] for _ in range(N)]
dist = [INF] * N

# Create Adjacency List
adj_list[0].append([1, 5]); adj_list[0].append([3, 1])
adj_list[1].append([2, 2])
adj_list[2].append([4, 2])
adj_list[3].append([1, 2]); adj_list[3].append([4, 7])

# Execute Dijkstra Algorithm with standard(start) node '0'
pq = PriorityQueue()
pq.put([0, 0])
dist[0] = 0

while not pq.empty():
    cur_dist, cur_node = pq.get()

    if cur_dist > dist[cur_node]:   # 추가된 부분
        continue

    for adj_node, adj_dist in adj_list[cur_node]:
        temp_dist = cur_dist + adj_dist
        if temp_dist < dist[adj_node]:
            pq.put([temp_dist, adj_node])
            dist[adj_node] = temp_dist

print(dist)
