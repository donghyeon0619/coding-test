# 쉬운 최단 거리
# 실버 1
# 첫번째 풀이
# from collections import deque
# import sys
#
# input = sys.stdin.readline
#
#
# def bfs(graph, s_x, s_y, dist_list, x_max, y_max, v_list):
#     dx = [0, 1, 0, -1]
#     dy = [-1, 0, 1, 0]
#
#     # 튜플을 넣을 때 리스트 안에 튜플을 넣어야 함
#     q = deque([(s_x, s_y)])
#     v_list[s_y][s_x] = True
#
#     while q:
#         x, y = q.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if (0 <= ny < y_max and 0 <= nx < x_max) and graph[ny][nx] == 1 and not (v_list[ny][nx]):
#                 dist_list[ny][nx] = dist_list[y][x] + 1
#                 q.append((nx, ny))
#                 v_list[ny][nx] = True
#
#
# n, m = map(int, input().split())
# matrix = [[0]*m for _ in range(n)]
# distance = [[0]*m for _ in range(n)]
# visited = [[False]*m for _ in range(n)]
#
# start_x = 0
# start_y = 0
#
# for i in range(n):
#     i_list = list(map(int, input().split()))
#     for j in range(m):
#         matrix[i][j] = i_list[j]
#         if i_list[j] == 1:
#             distance[i][j] = -1
#
#         if i_list[j] == 2:
#             start_x = j
#             start_y = i
#
#
# bfs(matrix, start_x, start_y, distance, m, n, visited)
#
# for i in range(n):
#     print(*distance[i])

## 두번째 풀이
## distance라는 따른 list를 선언하지 않고 visited로만 처리
from collections import deque
import sys
input = sys.stdin.readline


def bfs(graph, start, visited):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    q = deque([start])
    visited[start[1]][start[0]] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < m and 0 <= ny < n) and visited[ny][nx] == -1 and graph[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((nx, ny))


n, m = map(int, input().split())
graph = [[0]*m for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
start = tuple()

for i in range(n):
    graph[i] = list(map(int, input().split()))
    for j in range(m):
        if graph[i][j] == 2:
            start = (j, i)
        elif graph[i][j] == 0:
            visited[i][j] = 0

bfs(graph, start, visited)

for i in range(n):
    print(*visited[i])
