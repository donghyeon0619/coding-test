## 그림
## 실버 1
## 첫번째 풀이
## bfs를 이용한 정석 풀이
## 가장 빠름
import sys
from collections import deque

input = sys.stdin.readline


def bfs(pictures, s_y, s_x):
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    queue = deque([(s_x, s_y)])
    visited[s_y][s_x] = True
    total = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # nx, ny = x + dx[i], y+ dy[i]

            if (0 <= nx < m and 0 <= ny < n) and not visited[ny][nx] and pictures[ny][nx] == 1:
                queue.append((nx, ny))
                visited[ny][nx] = True
                total += 1

    return total


n, m = map(int, input().split())

# pictures = [[0]*m for _ in range(n)]
pictures = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]

cnt = 0
best = 0

# for i in range(n):
#     pictures[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if not visited[i][j] and pictures[i][j] == 1:
            cnt += 1
            # total = bfs(pictures, i, j)
            # if total > best:
            #     best = total
            best = max(best, bfs(pictures, i, j))


print(cnt)
print(best)


# ## 두번째 풀이
# ## set 스택(dfs)를 이용한 풀이
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

# 1인 칸 좌표만 모은 집합

ones = {(i, j) for i in range(n) for j in range(m) if grid[i][j] == 1}

count = 0
best = 0

# 4방향
dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

while ones:
    # 새 그림 덩어리 시작
    count += 1
    start = ones.pop()
    stack = [start]
    size = 1

    while stack:
        y, x = stack.pop()
        for dy, dx in dirs:
            ny, nx = y + dy, x + dx
            if (ny, nx) in ones:
                ones.remove((ny, nx))
                stack.append((ny, nx))
                size += 1

    best = max(best, size)

print(count)
print(best)

## 세번째 풀이
## union-find를 이용한 풀이
import sys
from collections import Counter
input = sys.stdin.readline


# Union-Find 구현
def find(a):
    while parent[a] != a:
        parent[a] = parent[parent[a]]
        a = parent[a]
    return a


def union(a, b):
    ra, rb = find(a), find(b),
    if ra != rb:
        parent[rb] = ra


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 1인 칸만 coords 리스트에 저장
coords = []
index_of = {}
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            idx = len(coords)
            coords.append((i, j))
            index_of[(i, j)] = idx

K = len(coords)
parent = list(range(K))

# 사방 탐색으로 UNION
dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]
for idx, (y, x) in enumerate(coords):
    for dx, dy in dirs:
        nx, ny = x + dx, y + dy
        j = index_of.get((ny, nx))
        if j is not None:
            union(idx, j)

# 루트별 크기 세기
roots = [find(i) for i in range(K)]
cnt = len(set(roots))
sizes = Counter(roots)
best = max(sizes.values()) if sizes else 0

print(cnt)
print(best)





