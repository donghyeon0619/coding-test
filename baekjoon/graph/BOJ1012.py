# 유기농 배추
# 실버 2
# 첫번째 풀이
# bfs를 이용해서 연결된 노드들을 전부 visited = 1로 바꿔두고 만약 연결되어있지 않은 것들은 탐색해서 visited= 0 일때만 순회하도록 설정
from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def bfs(b, a):

    global matrix, visited
    queue = deque()
    queue.append((b, a))
    visited[b][a] = True

    while queue:
        y, x = queue.popleft()

        for s in range(4):
            ny = y + dy[s]
            nx = x + dx[s]
            if (0 <= ny < N and 0 <= nx < M) and (not visited[ny][nx]) and matrix[ny][nx] == 1:
                queue.append((ny, nx))
                visited[ny][nx] = True


for _ in range(T):
    M, N, K = map(int, input().split())
    visited = [[False]*M for _ in range(N)]
    matrix = [[0]*M for _ in range(N)]
    cnt = 0

    for i in range(K):
        X, Y = map(int, input().split())
        matrix[Y][X] = 1

    for j in range(N):
        for k in range(M):
            if (not visited[j][k]) and matrix[j][k] == 1:
                cnt += 1
                bfs(j, k)

    print(cnt)

# 두번째 풀이
# dfs를 이용한 풀이
# 파이썬의 기본 재귀 한계는 1000단계인데, 해당 배추의 최대 갯수가 2500개이므로 최악의 경우 2500개 까지 재귀 depth가 이뤄질 수 있으므로
# 여기서는 재귀를 이용한 dfs를 구현하지 않고 스택을 이용해서 dfs를 구현하는 것이 적절함
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def dfs(sy, sx):
    stack = [(sy, sx)]
    while stack:
        y, x = stack.pop()
        # 1) 범위 벗어나거나 이미 방문했거나 배추가 없는 칸이면
        if not (0 <= y < N and 0 <= x < M):
            continue
        if visited[y][x] or field[y][x] == 0:
            continue

        visited[y][x] = True
        # 네 방향 모두 스택에 추가
        for i in range(4):
            stack.append((y + dy[i], x + dx[i]))


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    field = [[0]*M for _ in range(N)]
    visited = [[False]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input(). split())
        field[y][x] = 1

    worms = 0
    for y in range(N):
        for x in range(M):
            if field[y][x] == 1 and not visited[y][x]:
                worms += 1
                dfs(y, x)

    print(worms)

## 세번째 풀이
## 연결된 배추만 순회하기
import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    # 배추 좌표 리스트
    cabbages = []
    # 빠른 존재 검사용(탐색용)
    has_cabbage = set()
    for _ in range(K):
        x, y = map(int, input().split())
        cabbages.append((y, x))
        has_cabbage.add((y, x))

    visited = set()
    worms = 0

    for y, x in cabbages:
        if (y, x) in visited:
            continue
        worms += 1
        # 스택 기반 DFS
        stack = [(y, x)]
        visited.add((y, x))
        while stack:
            cy, cx = stack.pop()
            for di in range(4):
                ny, nx = cy + dy[di], cx + dx[di]
                if (ny, nx) in has_cabbage and (ny, nx) not in visited:
                    visited.add((ny, nx))
                    stack.append((ny, nx))

    print(worms)

## 4번쨰 풀이
## union-find 풀이
## 배추 좌표에 번호를 매겨서 인접해 있으면 union을하고 마지막에 루트를 세는 방식
import sys
input = sys.stdin.readline


def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    ra, rb = find(a), find(b)
    if ra != rb:
        parent[rb] = ra


T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    coords = []
    idx_of = {}
    for i in range(K):
        x, y = map(int, input().split())
        coords.append((y, x))
        idx_of[(y, x)] = i

    parent = list(range(K))
    # 인접 방향
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i, (y, x), in enumerate(coords):
        for di in range(4):
            ny, nx = y + dy[di], x+dx[di],
            j = idx_of.get((ny,nx))
            if j is not None:
                union(i, j)

    # 루트의 유니크 개수 = 필요한 지렁이 수
    roots = {find(i) for i in range(K)}
    print(len(roots))


