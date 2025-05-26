## 첫번쨰 풀이
# T = int(input())
#
# for t in range(1, T+1):
#     N = int(input())
#
#
#     # arr = [[0] * N] * N
#     arr = [[0] * N for _ in range(N)]
#
#     i = 0
#     j = 0
#     cnt = 0
#     while True:
#         cnt += 1
#         arr[i][j] = cnt
#         if cnt == N*N:
#             break
#         if i == 0 and j < N - 1:
#             j += 1
#         elif i == N - 1 and j > 0:
#             j -= 1
#         elif i == N-1 and j == 0:
#             i -= 1
#         elif i == 0 and j == N - 1:
#             i += 1
#
#         if 0 < i < N - 1 and 0 < j < N - 1:
#             if arr[i][j+1] == 0:
#                 j += 1
#                 continue
#             elif arr[i-1][j] == 0:
#                 i -= 1
#                 continue
#             elif arr[i][j-1] == 0:
#                 j -= 1
#                 continue
#             elif arr[i+1][j] == 0:
#                 i += 1
#                 continue
#
#     for i in range(N):
#         print(" ".join(map(str, arr[i])))


## 두번쨰 풀이
## 방향 전환 로직을 한군데로 모으기
T = int(input())
for t in range(1, T + 1):
    N = int(input())

    # 1) 2차원 배열 초기화
    arr = [[0]*N for _ in range(N)]

    # 2) 우 -> 하 -> 좌 -> 상 순서
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    d = 0       # 현재 방향 인덱스
    x = y = 0   # 현재 위치
    cnt = 1     # 채울 숫자

    while cnt <= N*N:
        arr[x][y] = cnt
        cnt += 1

        # 다음 칸
        dx, dy = dirs[d]
        nx, ny = x+dx, y+dy

        # 범위 벗어나거나 이미 채워져 있으면 방향 전환
        if not(0 <= nx < N and 0 <= ny < N) or arr[nx][ny] != 0:
            d = (d+1) % 4
            dx, dy = dirs[d]
            nx, ny = x + dx, y + dy

        x, y = nx, ny

    # 출력
    print(f"#{t}")
    for row in arr:
        print(" ".join(map(str, row)))



## 세번쨰 풀이
## dfs를 이용해서 풀기

import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, d, cnt):
    # 1) 기저 조건: 다 채웠으면 종료
    if cnt > N*N:
        return

    arr[x][y] = cnt

    # 2) 다음 좌표 계산
    dx, dy = dirs[d]
    nx, ny = x+dx, y+dy

    # 3) 범위 벗어나거나 이미 채워진 칸이면 화면 전환
    if not (0 <= nx < N and 0 <= ny < N) or arr[nx][ny] != 0:
        d = (d + 1) % 4
        dx, dy = dirs[d]
        nx, ny = x+dx, y+dy

    # 4) 재귀 호출
    dfs(nx, ny, d, cnt+1)


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    # 방향 백터
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    # 시작 재귀
    dfs(0, 0, 0, 1)

    # 출력
    print(f"#{t}")
    for row in arr:
        print(" ".join(map(str, row)))

## 네번쨰 풀이
## 다른 풀이랑 다른 스텝 방식
from itertools import cycle

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]

    # 1) 이동 횟수 리스트
    steps = [N] + sum([[i]*2 for i in range(N-1, 0, -1)], [])

    # 2) 방향 순환: 우, 하, 좌, 상
    dirs = cycle([(0, 1), (1, 0), (0, -1), (-1, 0)])

    # 3) 시작위치를 "(0, -1)"로 두고, 첫 이동이 (0,0)이 되게 끔
    x, y = 0, -1
    cnt = 1

    for step in steps:
        dx, dy = next(dirs)
        for _ in range(step):
            x += dx
            y += dy
            arr[x][y] = cnt
            cnt += 1

    print(f"#{tc}")
    for row in arr:
        print(" ".join(map(str, row)))

