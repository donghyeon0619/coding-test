"""
SWEA - 1868 - 파핑파핑 지뢰찾기
Author: donghyeon
Date: 2026-07-20

[문제 요약]


[핵심 관찰]


[풀이 비교]
    풀이 1 :


    풀이 2 :


[시간 복잡도]
    풀이 1:
[공간 복잡도]
    풀이 1 :

[복습 포인트]
    -
"""
# 첫번째 풀이
"""
문제: 1868 파핑 파핑 지뢰 찾기

"""

from collections import deque

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())

    matrix = [list(input()) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    spray = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

    cnt = 0

    def can_spray(start_x, start_y):
        for dx, dy in spray:
            nx, ny = start_x + dx, start_y + dy
            if 0 <= nx < N and 0 <= ny < N and matrix[ny][nx] == "*":
                return False
        return True

    def bfs(start_x, start_y):

        q = deque([(start_x, start_y)])

        while q:
            x, y = q.popleft()

            for dx, dy in spray:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                    visited[ny][nx] = True
                    if can_spray(nx, ny):
                        q.append((nx, ny))

        return


    for i in range(N):
        for j in range(N):
            if matrix[i][j] != "." or visited[i][j] or not can_spray(j, i):
                continue

            visited[i][j] = True
            cnt += 1

            bfs(j, i)

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == "." and not visited[i][j]:
                visited[i][j] = True
                cnt += 1

    print(f"#{test_case} {cnt}")

