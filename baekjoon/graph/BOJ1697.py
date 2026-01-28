# 숨바꼭질
# 첫번째 풀이
# 시간 복잡도: O(N + 3N) => O(N)
# 어떤 시작점에서 해당값을 구하기위해 여러가지 방법들을 제시하게 된다면
# 이를 그래프 관점으로 해석해서 탐색을 하도록 하는문제
# 표면적으로는 이차원배열에서 이분탐색을 해야할 것 같지만, 결국에는 그래프 문제로 접근해야함
# 그리고 가중치가 없는 그래프에서 "최단거리"이므로 BFS가 최단거리를 구할 수 있음
# 그리고 인접리스트로 그래프를 표현할 필요가 없음. 이미 그래프로 표현된 상태라

from collections import deque

def bfs(s):

    global N, K, ans

    q = deque()
    q.append((0, s))
    visited[s] = True

    while q:
        d, v = q.popleft()

        if v == K:
            print(d)
            return

        nx = [v - 1, v + 1, v * 2]

        for nv in nx:
            if 0 <= nv <= 100000 and not visited[nv]:
                q.append((d + 1,  nv))
                visited[nv] = True


N, K = map(int, input().split())
visited = [False for _ in range(100001)]


## N이 K보다 크게 되면 그냥 뺴기만 하는 것이 더 작음
if N >= K:
    print(N - K)
else:
    bfs(N)

## 두번째 풀이 (강의 풀이)
## 내가 생각한 방식과는 똑같지만
## 변수 명이라든가 코드구현면에서 좀더 깔끔한 풀이
from collections import deque

MAX = int(1e5)

N, K = map(int, input().split())

# solve
q = deque()
visited = [False] * (MAX + 1)

q. append((0, N))
visited[N] = True

while q:
    time, pos = q.popleft()

    if pos == K:
        print(time)
        exit()

    for nxt_pos in [pos - 1, pos + 1, pos * 2]:
        if (0 <= nxt_pos <= MAX) and (not visited[nxt_pos]):
            q.append((time + 1, nxt_pos))
            visited[nxt_pos] = True


