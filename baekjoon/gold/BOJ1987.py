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
# def dfs(x, y, depth):
#     global visited, R, C, matrix, chars, max_depth, dy, dx
#
#     # 1) 현재 칸 방문 처리 & 사용 문자 인덱스 기록
#     visited[y][x] = True
#     chars.append(matrix[y][x])
#     max_depth = max(max_depth, depth)
#
#     # 2) 네 방향 탐ㅁ색
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if 0 <= nx < C and 0 <= ny < R and (not visited[ny][nx] and matrix[ny][nx] not in chars):
#             dfs(nx, ny, depth + 1)
#
#     # 3) **백트래킹**: 호출이 돌아올 때마다 상태 원복
#     chars.pop()
#     visited[y][x] = False
#
#
# R, C = map(int, input().split())
# matrix = [list(input()) for _ in range(R)]
# max_depth = 1
# visited = [[False for _ in range(C)] for _ in range(R)]
# chars = []
#
# dx = [0, 1, 0, -1]
# dy = [-1, 0, 1, 0]
#
# visited[0][0] = True
# chars.append(matrix[0][0])
# dfs(0, 0, 1)
#
# print(max_depth)

# 세번째 풀이(강의 풀이)
# 알파벳의 대문자 개수는 26개
# dp로 풀기에는 어떤 rc로 왔는지에 대해서 표기를 해야하고 이걸 비트 마스크로 표현하면 2^26이 되므로 해당 배열에 엄청난 공간이 필요함
# 백트래킹 문제임
# 셋을 이용해서 구현
# 백트레킹 풀이를 구현할때 중요한것은 "구현의 효율성" 즉, 자료구조의 선택이 중요
# 이문제에서 set 이용하게 되면 시간초과가 발생하므로 리스트를 이용하는 것이 가장 적절

def search(y, x):
    global dy, dx, R, C, board, st, ans

    # base case
    if y < 0 or x < 0 or y >= R or x >= C:
        return
    # 이부분에서 최악의 경우 전부 대문자 26개를 전부 확인해야하므로 힘들수가 있음
    if board[y][x] in st:
        return
    st.add(board[y][x])

    ans = max(ans, len(st))

    # recursive case
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        search(ny, nx)

    st.remove(board[y][x])


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

R, C = map(int, input().split())
board = [input() for _ in range(R)]

st = set()
ans = 0

search(0, 0)

print(ans)

# 4번째 풀이 리스트를 이용한 풀이
# 26개의 대문자 체크배열을 선언하고 해당 대문자가 포함이 되었는지 체크
# ord()를 통해서 유니코드 정수로 반환 후 0~25사이에 인덱스 값중 하나가 포함이 되어있는지 확인하고 만약 포함이 안되어있으면
# cur_len을 늘리고 max()를 통해서 비교후에 더 높은 값을 답으로 지정해놓음
# 그리고 백트래킹과정에서는 해당 길이를 줄이고 체크배열의 해당 문자도 False로 변경
def search(y, x):
    global dy, dx, R, C, board, check, cur_len, ans

    # base case
    if y < 0 or x < 0 or y >= R or x >= C:
        return
    if check[ord(board[y][x]) - ord('A')]:
        return
    check[ord(board[y][x]) - ord('A')] = True
    cur_len += 1

    ans = max(ans, cur_len)

    # recursive case
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        search(ny, nx)

    cur_len -= 1
    check[ord(board[y][x]) - ord('A')] = False


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

R, C = map(int, input().split())
board = [input() for _ in range(R)]

check = [False] * 26
cur_len = 0
ans = 0

search(0, 0)
print(ans)


