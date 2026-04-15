"""
    제목: 사라지는 발판
    난이도: Hard (프로그래머스 난이도 3정도)
    리뷰: 턴제 방식에서 홀짝 방식에 대해서 어느정도 이해는 했지만 게임이론 문제에 대한 구현에 대해서 고민해보면 좋은 문제
    특징: 플레이어를 A와 B로 나누지 말고 "나"와 "상대방" 나눠서 생각하고 풀기
    다시 풀었는지: x
"""
# # 첫번째 풀이
# def solution(board, aloc, bloc):
#     answer = -1
#     raw = len(board)
#     col = len(board[0])
#     visited = [[False for _ in range(col)] for _ in range(raw)]
#
#     move(board, aloc[1], aloc[0], bloc[1], bloc[0], raw, col, visited)
#
#     return answer
#
#
# def move(board, me_pos_x, me_pos_y, you_pos_x, you_pos_y, raw, col, visited):
#     dx = [1, 0, -1, 0]
#     dy = [0, 1, 0, -1]
#
#     for i in range(4):
#         nx = me_pos_x + dx[i]
#         ny = me_pos_y + dy[i]
#         if (0 <= nx < col and 0 <= ny < raw) and not visited[ny][nx] and board[ny][nx] == 1:
#             visited[ny][nx] = True
#             move(board, you_pos_x, you_pos_y, nx, ny,  raw, col, visited)
#             visited[ny][nx] = False
#
#
# def play(board, aloc, bloc):

## 두번쨰 풀이
def solution(board, aloc, bloc):
    n, m = len(board), len(board[0])

    def dfs(ax, ay, bx, by):
        if board[ax][ay] == 0:
            return False, 0

        best_win = float('inf')     # 이기는 수 중 최소
        best_lose = 0               # 지는 수 중 최대

        for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1),):
            nx, ny = ax+dx, ay+dy
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny]:
                board[ax][ay] = 0
                opp_win, cnt = dfs(bx, by, nx, ny)
                board[ax][ay] = 1

                if not opp_win:
                    best_win = min(best_win, cnt + 1)
                else:
                    best_lose = max(best_lose, cnt + 1)

        if best_win < float('inf'):
            return True, best_win
        return False, best_lose

    return dfs(*aloc, *bloc)[1]

## 세번째 풀이 (강의 풀이)
from copy import deepcopy

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def in_range(y, x):
    global R, C
    return 0 <= y < R and 0 <= x < C

def func(board, cury, curx, opy, opx): # 현재 상태에서 최적의 게임을 했을 때 (결과, 최대 이동횟수)
    global R, C

    # base case
    if board[cury][curx] == 0:
        return False, 0

    # recursive case
    cboard = deepcopy(board)
    cboard[cury][curx] = 0

    win_case = []
    lose_case = []
    for i in range(4):
        ny = cury + dy[i]
        nx = curx + dx[i]
        if in_range(ny, nx) and cboard[ny][nx] == 1:
            nres, ncnt = func(cboard, opy, opx, ny, nx)
            if not nres:
                win_case.append(ncnt)
            else:
                lose_case.append(ncnt)

    if win_case:    # 이기는 경우가 있다면, 최대한 빨리 이겨야 함.
        return True, min(win_case) + 1
    if lose_case:   # 이기는 경우가 없다면, 최대한 오래 버티도록 해야 함.
        return False, max(lose_case) + 1
    return False, 0

def solution(board, aloc, bloc):
    global R, C
    R = len(board)
    C = len(board[0])

    return func(board, *aloc, *bloc)[1]