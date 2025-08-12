"""
문제: 알파벳
난이도: 골드 5
중요도: 별 5
문제평: 비트마스크라는 새로운 기술 도입됨
"""
# 첫번쨰 풀이
# stack을 이용해서 풀어보려 했지만 결국엔 구현 못함 아래 함수를 통한 풀이도 구현을 하지 못했음
# R, C = map(int, input().split())
# matrix = [list(input()) for _ in range(R)]
# depths = [[0 for _ in range(C)] for _ in range(R)]
# visited = [[False for _ in range(C)] for _ in range(R)]
# chars = []
#
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]
#
# stack = [(0, 0)]
# depths[0][0] = 1
# chars.append(matrix[0][0])
#
# while stack:
#     x, y = stack.pop()
#
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < C and 0 <= ny < R:
#             if matrix[ny][nx] not in chars and not visited[ny][nx]:
#                 depths[ny][nx] = depths[y][x] + 1
#                 stack.append((nx, ny))
#                 chars.append(matrix[ny][nx])
#                 visited[ny][nx] = True
#                 break
#
# print(depths)
# # 이차원 리스트 최대값은 map을 이용
# print(max(map(max, depths)))

# 두번째풀이(시간초과 남)
# 백트래킹을 이용한 풀이
# 기존까지 dfs는 인접리스트를 이용했는데 이건 네방향 다 갈 수 있으므로
# 인접리스트를 사용하지 않음
def dfs(x, y, depth):
    global visited, R, C, matrix, chars, max_depth, dy, dx

    # 1) 현재 칸 방문 처리 & 사용 문자 인덱스 기록
    visited[y][x] = True
    chars.append(matrix[y][x])
    max_depth = max(max_depth, depth)

    # 2) 네 방향 탐ㅁ색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and (not visited[ny][nx] and matrix[ny][nx] not in chars):
            dfs(nx, ny, depth + 1)

    # 3) **백트래킹**: 호출이 돌아올 때마다 상태 원복
    chars.pop()
    visited[y][x] = False


R, C = map(int, input().split())
matrix = [list(input()) for _ in range(R)]
max_depth = 1
visited = [[False for _ in range(C)] for _ in range(R)]
chars = []

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

visited[0][0] = True
chars.append(matrix[0][0])
dfs(0, 0, 1)

print(max_depth)
