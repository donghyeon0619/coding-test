# 파티
# 골드 3
# 시간 복잡도: O(NMlogN)
# -> 여기서는 시간복잡도가 최악의 경우 1억이 나오므로 제한시간이 1초인데 안될 수도 있음
# 첫번째 풀이
import sys
from queue import PriorityQueue

input = sys.stdin.readline


def dijkstra(start, dist):

    global adj_list

    pq = PriorityQueue()
    pq.put([0, start])
    dist[start] = 0

    while not pq.empty():

        cur_dist, cur_node = pq.get()

        if cur_dist > dist[cur_node]:
            continue

        for next_node, next_dist in adj_list[cur_node]:
            temp_dist = cur_dist + next_dist
            if temp_dist < dist[next_node]:
                pq.put([temp_dist, next_node])
                dist[next_node] = temp_dist


INF = int(1e12)

N, M, X = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
dist_s = [[INF] * (N + 1) for _ in range(N + 1)]
dist_e = [INF for _ in range(N + 1)]
total_time = [0 for _ in range(N + 1)]

for i in range(M):
    s, e, w = map(int, input().split())
    adj_list[s].append([e, w])

for i in range(1, N + 1):
    dijkstra(i, dist_s[i])

dijkstra(X, dist_e)

for i in range(1, N+1):
    total_time[i] = dist_s[i][X] + dist_e[i]


print(max(total_time[1:]))

# 두번째 풀이
# 시간복잡도 : O(MlogN)
# 다익스트라를 N번 돌리는 것은 비효율적임
# 역으로 그래프를 뒤집는 역방향 그래프도 생각해볼 필요가 있다.
# 다익스트라의 정의를 가지고 활용하는 방법
import sys
from queue import PriorityQueue

input = sys.stdin.readline


def dijkstra(start, dist, adj_li):

    pq = PriorityQueue()
    pq.put([0, start])
    dist[start] = 0

    while not pq.empty():

        cur_dist, cur_node = pq.get()

        if cur_dist > dist[cur_node]:
            continue

        for next_node, next_dist in adj_li[cur_node]:
            temp_dist = cur_dist + next_dist
            if temp_dist < dist[next_node]:
                pq.put([temp_dist, next_node])
                dist[next_node] = temp_dist


INF = int(1e12)

N, M, X = map(int, input().split())

adj_list = [[] for _ in range(N + 1)]
reverse_adj_list = [[] for _ in range(N + 1)]
dist_s = [INF for _ in range(N + 1)]
dist_e = [INF for _ in range(N + 1)]
total_time = [0 for _ in range(N + 1)]

for i in range(M):
    s, e, w = map(int, input().split())
    adj_list[s].append([e, w])
    reverse_adj_list[e].append([s, w])

dijkstra(X, dist_s, reverse_adj_list)
dijkstra(X, dist_e, adj_list)

#
# for i in range(1, N+1):
#     total_time[i] = dist_s[i] + dist_e[i]
#
#
# print(max(total_time[1:]))
## 아래 코드는 위랑 같은 로직
## N이 아주클 때는(슬라이스 복사 비용 때문에 아래가 더 짧게 시간이 형성될 수 있음)
ans = -1
for i in range(1, N + 1):
    ans = max(ans, dist_s[i] + dist_e[i])

print(ans)
