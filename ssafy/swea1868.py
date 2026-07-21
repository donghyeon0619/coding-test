"""
SWEA - 1868 - 파핑파핑 지뢰찾기
Author: donghyeon
Date: 2026-07-20

[문제 요약]
    N*N 지뢰밭에서 지뢰가 없는 모든 칸에 숫자가 표시되도록 만들 때
    필요한 최소 클릭 수를 구한다.
    - 빈 칸을 클릭하면 주변 8칸의 지뢰 수가 표시된다.
    - 그 수가 0이면 주변 8칸이 자동으로 열리고, 열린 칸이 또 0이면 연쇄로 퍼진다.
    - 지뢰 칸은 클릭 대상이 아니다(빈 칸만 모두 열면 된다).

[핵심 관찰]
    빈 칸은 클릭 관점에서 딱 두 종류로 나뉜다.
      1) 0인 칸 : 주변에 지뢰가 하나도 없는 칸. 클릭하면 연결된 덩어리 전체 +
                 그 경계의 숫자칸까지 한 번에 열린다  → 덩어리(연결 성분)당 클릭 1번.
      2) 숫자칸 : 주변에 지뢰가 있는 빈 칸. 클릭해도 자기 자신만 열린다.
                 단, 8방향 중 하나라도 0인 칸이 있으면 그 연쇄에 묻어서 자동으로 열린다.
    따라서
        최소 클릭 수 = (0인 칸 덩어리의 개수) + (연쇄로 열리지 못한 숫자칸의 개수)

[풀이 비교]
    풀이 1 : 실제로 열어보며 세기 (BFS + 나머지 카운트)  ← 이 파일
        1단계) 아직 안 열린 0인 칸을 찾을 때마다 클릭 1회, BFS로 연쇄를 퍼뜨려
               덩어리 전체 + 경계 숫자칸을 visited 처리한다.
        2단계) 그러고도 안 열린 숫자칸을 하나씩 세어 개별 클릭으로 더한다.

[시간 복잡도]
    풀이 1 : O(N^2). 모든 칸을 BFS에서 최대 한 번 방문하고, 칸마다 8방향을
             확인(can_spray도 O(8))하므로 상수 배수만 붙는다.

[공간 복잡도]
    풀이 1 : O(N^2). matrix + visited 배열.

[복습 포인트]
    - 1단계 스킵 조건은 "지뢰이거나 / 이미 열렸거나 / 0이 아닌 칸"을 or 로 묶는다.
    - 좌표는 (행, 열)로 일관되게. matrix[y][x] 와 bfs(x, y) 처럼 섞으면 헷갈린다.
    - "0인 칸 = 연결 성분당 클릭 1번", "숫자칸 = 이웃에 0 있으면 공짜" 두 문장이 핵심
"""
# 첫번째 풀이
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

