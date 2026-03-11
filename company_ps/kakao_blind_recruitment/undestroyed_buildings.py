"""
    제목: 파괴되지 않은 건물

"""
## 첫번째 풀이
## 예상했던 대로 시간초과가 난 풀이
# def solution(board, skill):
#     answer = 0
#     for tp, r1, c1, r2, c2, degree in skill:
#         for i in range(r1, r2+1):
#             for j in range(c1, c2+1):
#                 if tp == 1:
#                     board[i][j] -= degree
#                 else:
#                     board[i][j] += degree
#
#     for board_row in board:
#         for board_column in board_row:
#             if board_column > 0:
#                 answer += 1
#
#     return answer

# 두번째 풀이(대중적인 풀이)
# 풀이: 2D 이모스법 (Imos Method)
# 차분 배열(diff)에 스킬 범위의 꼭짓점 4곳만 표시 후,
# 행/열 방향 누적합으로 실제 변화량을 복원하여 board에 반영
def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])

    # diff 배열 생성 (N+1) x (M+1)
    diff = [[0] * (M + 1) for _ in range(N + 1)]

    # ① skill → diff 꼭짓점 표시
    for tp, r1, c1, r2, c2, degree in skill:
        v = -degree if tp == 1 else degree
        diff[r1][c1] += v
        diff[r1][c2 + 1] -= v
        diff[r2 + 1][c1] -= v
        diff[r2 + 1][c2 + 1] += v

    # ② 행 방향 누적합
    for i in range(N):
        for j in range(1, M + 1):
            diff[i][j] += diff[i][j - 1]

    # ③ 열 방향 누적합
    for i in range(1, N + 1):
        for j in range(M):
            diff[i][j] += diff[i - 1][j]

    # ④ board + diff 더해서 카운트
    for i in range(N):
        for j in range(M):
            if board[i][j] + diff[i][j] > 0:
                answer += 1

    return answer

# 세번째 풀이 (강의 풀이)
# 똑같이 이모스법을 이용했지만
# 위에와는 다르게 일반적인 2d 일반 누적합을 이용해서 풀었음
def solution(board, skill):
    R = len(board)
    C = len(board[0])
    dp = [[0] * (C + 2) for _ in range(R + 2)]  # 차이 배열

    # 쿼리에 대해 차이 배열(dp)에 갱신
    for t, r1, c1, r2, c2, d in skill:
        if t == 1: d = -d
        r1, c1, r2, c2 = r1 + 1, c1 + 1, r2 + 1, c2 + 1
        dp[r1][c1] += d
        dp[r1][c2 + 1] -= d
        dp[r2 + 1][c1] -= d
        dp[r2 + 1][c2 + 1] += d

    for y in range(1, R + 1):
        for x in range(1, C + 1):
            dp[y][x] += (dp[y][x - 1] + dp[y - 1][x] - dp[y - 1][x - 1])

    ans = R * C
    for y in range(R):
        for x in range(C):
            ans -= (board[y][x] + dp[y + 1][x + 1] <= 0)

    return ans
