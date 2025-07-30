"""

문제: 사탕 게임
난이도: 실버 2

"""
# 첫번째 풀이
# (직접 풀어봤지만 안풀림)
# 아직까지 구현에 있어서 힘들다..
# N = int(input())
#
# arr = [input() for _ in range(N)]
#
# for i in range(N - 1):
#     for j in range(N-1):
#         if arr[i][j] != arr[i][j + 1]:
#             temp = [arr[i][j + 1]]

# 두번째 풀이 (강의 풀이)
# 브루트 포스 풀이
# 2차원 배열에서 상하좌우 접근하는 방법 활용
# 연속된 부분 중에서, 모두 같은 값으로 이루어져 있는 가장 긴 길이 구함
# 이 풀이는 각 인접한 값을 바꾸고 모든 배열을 순회하면서 가장 긴 인접한 배열 크기를 구하는 풀이
# 시간복잡도: O(N^4)
# def get_best():
#     global N, matrix
#     best = 0
#
#     # rows
#     for i in range(N):
#         bef = '-'
#         value = 0
#         for j in range(N):
#             if bef == matrix[i][j]:
#                 value += 1
#             else:
#                 value = 1
#             bef = matrix[i][j]
#             best = max(best, value)
#
#     # columns
#     for j in range(N):
#         bef = '-'
#         value = 0
#         for i in range(N):
#             if bef == matrix[i][j]:
#                 value += 1
#             else:
#                 value = 1
#             bef = matrix[i][j]
#             best = max(best, value)
#
#     return best
#
#
# dy = [-1, 0, 1, 0]
# dx = [0, 1, 0, -1]
#
# N = int(input())
# matrix = [list(input()) for _ in range(N)]
# ans = 0
#
# for y in range(N):
#     for x in range(N):
#         for i in range(4):
#             ny = y + dy[i]
#             nx = x + dx[i]
#             if 0 <= ny < N and 0 <= nx < N:
#                 if matrix[y][x] != matrix[ny][nx]:
#                     matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x],
#                     ans = max(ans, get_best())
#                     matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x],
#
# print(ans)

# 세번째 풀이
# 상하좌우 방향 방법을 쓰지만
# 바꾸고 전체 이차원 배열을 순회하는 것이 아닌
# 바꾼 행과 열을 순회 하는 것
def get_best(y, x):
    global N, matrix
    best = 0

    # one row
    bef = '-'
    value = 0
    for j in range(N):
        if bef == matrix[y][j]:
            value += 1
        else:
            value = 1
        bef = matrix[y][j]
        best = max(best, value)

    # one column
    bef = '-'
    value = 0
    for i in range(N):
        if bef == matrix[i][x]:
            value += 1
        else:
            value = 1
        bef = matrix[i][x]
        best = max(best, value)

    return best


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N = int(input())
matrix = [list(input()) for _ in range(N)]
ans = 0

for y in range(N):
    for x in range(N):
        if y == x:
            ans = max(ans, get_best(y, x))
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if matrix[y][x] != matrix[ny][nx]:
                    matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]
                    ans = max(ans, get_best(y, x))
                    matrix[y][x], matrix[ny][nx] = matrix[ny][nx], matrix[y][x]

print(ans)
