# 토마토
# 골드 5
# 시간복잡도: O(MN + 4NM) = O(MN)
# 첫번째 풀이(못 풀었던 문제)

# import sys
# input = sys.stdin.readline
# from collections import deque
#
# def dfs(x, y):
#     global visited, matrix, M, N, ans, dx, dy
#
#     q = deque()
#     q.append((x, y))
#     visited[y][x] = True
#
#     cnt = 0
#
#     while q:
#         x, y = q.popleft()
#
#         for k in range(4):
#             nx, ny = x + dx[k], y + dy[k]
#             if (0 <= nx < M) and (0 <= ny < N) and not visited[ny][nx]:
#                 if matrix[ny][nx] == 0:
#                     visited[ny][nx] = True
#                     q.append((nx, ny))
#                     matrix[ny][nx] = 1
#                     cnt += 1
#                 elif matrix[ny][nx] == 1:
#                     cnt = (cnt + 1) // 2
#                     return cnt
#
#     return cnt
#
#
# M, N = map(int, input().split())
#
# matrix = [list(map(int, input().split())) for _ in range(N)]
# visited = [[False] * M for _ in range(N)]
#
# dx = [1, 0, -1, 0]
# dy = [0, 1, 0, -1]
#
# ans = 0
#
# for i in range(N):
#     for j in range(M):
#         if matrix[i][j] == 1 and not visited[i][j]:
#             ans = max(ans, dfs(j, i))
#
# for i in range(N):
#     for j in range(M):
#         if matrix[i][j] == 0:
#             print(-1)
#             exit()
#
# print(ans)
#

## 두번쨰 풀이
## 기존에 푼 dfs 문제는 모든 값에서 루프를 돌아서 해당 값이 1일떄 dfs를 돌러고 했음. 근데 이렇게 돌러고 하면
## 고려해야할 것이 많아서, 문제가 됨.
## 그래서 여기서는 1일때 값을 전부 queue에 넣고, 동시 dfs를 해서 그때마다 일수를 갱신하도록 해야함.
## 그리고 일반적인 그래프 탐색과는 다르게 방문 기록 리스트가 필요 없는 문제
## 처음 풀 때 이 사고과정이 아닌거 같으면 다시 다른 방법으로 바꿀 생각을 해봐야할 것 같다고 느꼈던 문제
import sys
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())

matrix = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

ans = 0

q = deque()

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 1:
            q.append((j, i))

while q:
    x, y = q.popleft()

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if (0 <= nx < M) and (0 <= ny < N) and not matrix[ny][nx]:
            matrix[ny][nx] = matrix[y][x] + 1
            q.append((nx, ny))

for i in range(N):
    for j in range(M):
        if matrix[i][j] == 0:
            print(-1)
            exit()
        elif matrix[i][j] > 0:
            ans = max(ans, matrix[i][j])

print(ans - 1)


## 세번째 풀이(강의 풀이)
## 여기서는 time이라는 변수를 만들어서 시작값과, 그리고 방문여부를 전부 고려하는 풀이
from collections import deque

INF = int(1e12)

# input
M, N = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

# solve
q = deque()
time = [[INF] * M for _ in range(N)]

for y in range(N):
    for x in range(M):
        if matrix[y][x] == 1:
            q.append((y, x))
            time[y][x] = 0

while q:
    y, x = q.popleft()

    # dx, dy 변수를 따로 안만들고 다른 풀이
    nx_ts = [(y - 1, x), (y, x + 1), (y + 1, x), (y, x - 1)]
    for ny, nx in nx_ts:
        if not (0 <= nx < M and 0 <= ny < N):
            continue
        if time[ny][nx] <= time[y][x] + 1:
            continue
        if matrix[ny][nx] == -1:
            continue
        q.append((ny, nx))
        time[ny][nx] = time[y][x] + 1


ans = -1
for y in range(N):
    for x in range(M):
        if matrix[y][x] != - 1:
            ans = max(ans, time[y][x])

print(ans if ans != INF else - 1)

