# 체스판 다시 칠하기 (구현 못함 다시 풀어봐야하는 문제)
# 실버 4
# 어떻게 구현해야할 지는 알 것 같은데 구현을 못함
# 이차원 배열에서 번갈아 데이터 삽입하는 로직이 들어감
# 발상은 쉬운편이지만 구현난이도가 높은 문제
# N, M = map(int, input().split())
#
# arr = [list(input()) for _ in range(N)]
# nums = [[0] * (N - 7) for _ in range(M - 7)]
#
# temp = [[""] * 8 for _ in range(8)]
#
# for n in range(0, N - 7):
#     for m in range(0, M - 7):
#         for i in range(n, n + 7):
#             for j in range(m, m + 7):
#                 if temp[i][j] == "":
#                     temp[i][j] = arr[i][j]
#                 elif temp[i][j] == arr[i + 1][j]:
#                     nums[n][m] += 1
#                     if temp[i][j] == "B":
#                         temp[i + 1][j] = "W"
#                     else:
#                         temp[i + 1][j] = "B"
#                 elif temp[i][j] == arr[i][j + 1]:
#                     nums[n][m] += 1
#                     if temp[i][j] == "B":
#                         temp[i][j + 1] = "W"
#                     else:
#                         temp[i][j + 1] = "B"
#
#
# print(min(min(row) for row in nums))
"""
- 강의 풀이
- 맨위 왼쪽이 'B'랑 'W'일 경우 두가자라고 문제에서 언급을 했는데 이를 활용하도록 해야함
- 그러므로 두 가지 경우의 체스를 만들고 비교하는 것이 가장 적절
- 그리고 범위를 지정할떄 감으로 하지 말고 직접 연습장에서
- 예시를 그려서 범위 지정해야 할듯
- 브루트 푸스로 푸는 문제
"""

# 함수를 뺴서 작성
def get_min(sy, sx):
    global board, chess1, chess2
    case1 = case2 = 0

    for i in range(8):
        for j in range(8):
            case1 += (board[sy + i][sx + j] != chess1[i][j])
            case2 += (board[sy + i][sx + j] != chess2[i][j])

    return min(case1, case2)


# 초기 가능한 체스 경우 세팅
chess1 = [['' for _ in range(8)] for _ in range(8)]
chess2 = [['' for _ in range(8)] for _ in range(8)]

# 2차원 배열에서 인접한 칸을 다르게 설정하는 방법
for i in range(8):
    for j in range(8):
        chess1[i][j] = ('W' if (i + j) % 2 == 0 else 'B')
        chess2[i][j] = ('B' if (i + j) % 2 == 0 else 'W')

N, M = map(int, input().split())
board = [input() for _ in range(N)]

best = int(1e12)
for y in range(N):
    for x in range(M):
        # 접근 시 끝 지점 접근하지 못하도록 처리
        if (y + 7 >= N) or (x + 7 >= M):
            continue
        best = min(best, get_min(y, x))

print(best)

"""
- 다른 사람 풀이
- 짝수 홀수를 기준으로 온바른 색을 판별하는 풀이
"""
n, m = map(int, input().split())
board = []
result = []

for _ in range(n):
    board.append(input())

for i in range(n - 7):
    for j in range(m - 7):
        draw1 = 0
        draw2 = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != 'B':
                        draw1 += 1
                    if board[a][b] != 'W':
                        draw2 += 1
                else:
                    if board[a][b] != 'W':
                        draw1 += 1
                    if board[a][b] != 'B':
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)


print(min(result))

