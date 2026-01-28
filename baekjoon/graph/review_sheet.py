## boj 2178
from collections import deque

def bfs(sx, sy):

    global matrix, visited, dist, M, N

    d = [(1, 0), (0, -1), (-1, 0), (0, 1)]

    q = deque()

    q.append((sx, sy))
    visited[sy][sx] = True
    dist[sy][sx] = 1

    while q:
        x, y = q.popleft()
        for ndx, ndy in d:
            nx, ny = x + ndx, y + ndy
            if 0 < nx <= M and 0 < ny <= N and not visited[ny][nx] and matrix[ny][nx] == "1":
                visited[ny][nx] = True
                q.append((nx, ny))
                dist[ny][nx] = dist[y][x] + 1

    print(dist[N][M])


N, M = map(int, input().split())

matrix = ['0' * (M + 1)] + ['0' + input() for _ in range(N)]
visited = [[False] * (M + 1) for _ in range(N + 1)]
dist = [[0] * (M + 1) for _ in range(N + 1)]

bfs(1, 1)