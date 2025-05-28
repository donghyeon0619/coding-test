## 미로 탐색
## 실버 1
## 첫번째 풀이(못 푼 문제)
## 상하 좌우로 1일때 존재하므로 간선 문제라 볼 수 있음
## 그러면 그래프 알고리즘 생각
## 가중 그래프가 아닌 경우에서 최단 경로는 bfs를 사용
## 행렬에서 탐색은 보통 그래프 탐색 문제로 생각할 수 있음
import sys

from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    global adj_list, distance
    q = deque([(1, 1)])
    distance[1][1] = 1

    while q:
        x, y = q.popleft()
        # 도착점에 도달했다면 조기, 종료도 가능
        if x == N and y == M:
            return distance[N][M]

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy

            # 1) 범위 검사 : 내부에 있을 때만 다음으로 진행
            if not (1 <= nx <= N and 1 <= ny <= M):
                continue

            # 범위 & 길 확인 & 미방문
            if adj_list[nx][ny] == 1 and distance[nx][ny] == 0:
                distance[nx][ny] = distance[x][y] + 1
                q.append((nx, ny))
    return distance[N][M]


N, M = map(int, input().split())
adj_list = [[0]*(M+1) for _ in range(N+1)]
distance = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    c = input().rstrip()
    for j in range(M):
        adj_list[i][j+1] = int(c[j])

print(bfs())

## 두번째 풀이
## 인접리스트를 굳이 만들 필요가 없음,
# 인접 리스트를 사용하는 목적은 그래프를 표현하기 위해서 사용하는 것
# 이미 2차원 배열에서 그래프를 표현한 상태라 인접리스트 사용 필요 x
from collections import deque
import sys
input = sys.stdin.readline

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def solve():
    q = deque()
    visited = [[False] * (M+1) for _ in range(N + 1)]

    # (distance, y, x)
    q.append((1, 1, 1))
    visited[1][1] = True

    while q:
        distance, y, x = q.popleft()

        if y == N and x == M:
            return distance

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if (1 <= ny <= N and 1 <= nx <= M) and (not visited[ny][nx]) and (matrix[ny][nx] == '1'):
                q.append((distance + 1, ny, nx))
                visited[ny][nx] = True

    return -1


# input

N, M = map(int, input().split())
# 0번 행과 0번 열에 "가드용"0을 채워서 1부터 N, 1부터 M까지만 미로가 보이도록 만드는 편법
matrix = ['0' * (M+1)] + ['0' + input() for _ in range(N)]

print(solve())




