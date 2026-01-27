## boj 2178
from collections import deque

def bfs(sx, sy):

    global matrix, visited

    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    q = deque()

    cnt = 0
    q.append((sx, sy))
    visited[sy][sx] = True

    while q:
        x, y = q.popleft()
        for ndx, ndy in dx, dy:
            if




N, M = map(int, input().split())

matrix = ['0' * (M + 1)] + ['0' + input() for _ in range(N)]
visited = [[False] * (M + 1) for _ in range(N + 1)]

