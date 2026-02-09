# 숨바꼭질 3
# 골드 5
# 첫번쨰 풀이
from queue import PriorityQueue

INF = int(1e12)

MAX = 100001
N, K = map(int, input().split())
dist = [INF for _ in range(MAX)]

pq = PriorityQueue()
pq.put([0, N])
dist[N] = 0

while not pq.empty():

    cur_dist, cur_node = pq.get()

    if cur_dist > dist[cur_node]:
        continue

    nx = [cur_node + 1, cur_node - 1, cur_node * 2]

    for i in range(3):
        if nx[i] >= MAX or nx[i] < 0:
            continue

        if i == 0 or i == 1:
            temp_dist = cur_dist + 1
        else:
            temp_dist = cur_dist

        if temp_dist < dist[nx[i]]:
            pq.put([temp_dist, nx[i]])
            dist[nx[i]] = temp_dist

print(dist[K])


# 두번째 풀이(강의 풀이)
# 내가 생각한 풀이랑 같으면서
# 여기는 FOR문을 두번사용하지 않고, NEXTS 변수라는 함수에 다음 위치랑 다음시간을 튜플형태로 두개 저장하는 형태로 진행
from queue import PriorityQueue

INF = int(1e12)
MAX = int(1e5)

# input
N, K = map(int, input().split())

# solve
time = [INF] * (MAX + 1)
pq = PriorityQueue()
time[N] = 0
pq.put([0, N])

while not pq.empty():
    cur_time, cur_pos = pq.get()

    nexts = [
        (cur_time, 2 * cur_pos),
        (cur_time + 1, cur_pos + 1),
        (cur_time + 1, cur_pos - 1)
    ]

    for next_time, next_pos in nexts:
        if 0 <= next_pos <= MAX:
            if next_time < time[next_pos]:
                time[next_pos] = next_time
                pq.put([next_time, next_pos])


print(time[K])

# 세번쨰 풀이
# SET, BFS를 이용한 풀이
# 0-1 BFS (최소 수정 버전: set -> dist, 종료조건 x==K)
# cost가 0이면 같은레벨(depth,dist)이므로 appendleft를 통해 우선순위를 높여야함
from collections import deque

N, K = map(int, input().split())

MAX = 100000
INF = 10**9
dist = [INF] * (MAX + 1)

dq = deque()
dq.append(N)
dist[N] = 0

while dq:
    x = dq.popleft()

    if x == K:
        break

    for nx in (2 * x, x - 1, x + 1):
        if 0 <= nx <= MAX:
            cost = 0 if nx == 2 * x else 1
            nd = dist[x] + cost
            if nd < dist[nx]:
                dist[nx] = nd
                if cost == 0:
                    dq.appendleft(nx)
                else:
                    dq.append(nx)

print(dist[K])

