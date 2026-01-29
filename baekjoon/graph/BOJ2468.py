## 안전 영역
## 실버 1
## 첫번째 풀이
## 시간복잡도: O (100 * N^2)
# -----------------------------
# 사고 과정(접근 아이디어)
# -----------------------------
# 1) 비의 양(기준 높이) h가 정해지면
#    - 높이 <= h 인 칸은 잠김(침수)
#    - 높이  > h 인 칸만 안전(비침수)
#
# 2) "안전 영역"의 개수는
#    높이 > h 인 칸들만 모아 놓았을 때,
#    상/하/좌/우로 연결된 연결요소(컴포넌트)의 개수와 같다.
#
# 3) 따라서 각 h마다:
#    - visited를 새로 초기화
#    - 모든 칸을 훑으며 (아직 방문 X) && (높이 > h) 인 칸을 찾으면
#      BFS로 그 칸과 연결된 모든 안전 칸을 방문 처리
#      -> BFS 1번 수행 = 안전 영역 1개 발견이므로 cnt += 1
#
# 4) 모든 h에 대해 cnt 중 최댓값(ans)을 갱신하면 된다.
#
# 5) visited는 "같은 h에서" 중복 카운트를 막기 위한 장치라서,
#    h가 바뀌면 안전/침수 상태와 연결관계가 달라질 수 있으므로
#    매 h마다 visited를 초기화해야 한다.
# -----------------------------
from collections import deque


def bfs(sx, sy, h):
    global visited, matrix, cnt, dx, dy

    q = deque()
    q.append((sx, sy))
    visited[sy][sx] = True

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]

            if (0 <= nx < N) and (0 <= ny < N) and not visited[ny][nx] and matrix[ny][nx] > h:
                q.append((nx, ny))
                visited[ny][nx] = True


N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

ans = 0

# 가장 높은 H값을 구하는 방법
H = max(map(max, matrix))

for h in range(H):

    cnt = 0
    visited = [[False] * N for _ in range(N)]

    for ni in range(N):
        for nj in range(N):
            if not visited[ni][nj] and matrix[ni][nj] > h:
                bfs(nj, ni, h)
                cnt += 1

    ans = max(ans, cnt)

print(ans)

## 두번쨰 풀이
## 같은 로직이고 이것은 bfs가 아닌 dfs를 이용한 풀이
import sys
sys.setrecursionlimit(int(1e6))

def dfs(x, y, h):
    global dx, dy, N, matrix, visited

    # base case
    if not (0 <= x < N and 0 <= y < N):
        return
    if visited[y][x] or matrix[y][x] <= h:
        return

    visited[y][x] = True

    # recursive case
    for i in range(4):
        ny, nx = x + dx[i], y + dy[i]
        dfs(ny, nx, h)



def get_num(height):
    global dy, dx, N, matrix, visited

    visited[height] = [[False] * N for _ in range(N)]

    num = 0
    for y in range(N):
        for x in range(N):
            if (not visited[y][x]) and (matrix[y][x] > height):
                dfs(x, y, height)
                num += 1

    return num


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for height in range(101):
    ans = max(ans, get_num(height))

print(ans)



