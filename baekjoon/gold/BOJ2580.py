"""
문제: 스토커
난이도: 골드 5
중요도: 별 5
핵심 특징: 살펴보지 않아도 되는 경우를 가지 치기 할 수 있을 시 -> 최악의 시간 복잡도를 계산할 수 없으므로 빽트래킹으로 풀어야 함
"""
# 첫번째 풀이 (내 풀이) 풀어보지 못함
# 처음에 0인 col, row, block단위로 나눠서, 해당 행, 열, 블록에서 안 쓰였던 숫자를 저장하고 그 값을 가지고
# 백트래킹 방식으로 값을 찾는방법을 생각했지만 구현을 하지 못했음
# 비효율적인 것이 처음에 0인값을 찾아서 그 값을 넣어놓는다면, 만약 아닌 값은 썼다고 True 설정하는 것이
# 탐색을 여러번 할필요가 없게 됨
#
# stoku = [list(map(int, input().split())) for _ in range(9)]
# num = []
#
# col_l = [[] for _ in range(9)]
# row_l = [[] for _ in range(9)]
# block_l = [[] for _ in range(9)]
#
# def stuff():
#     global num, col_l, row_l, block_l
#
#     x, y = num.pop()
#
#     for i in range(0, 9):
#         if not (i in col_l[x] and i in row_l[y] and i in block_l[3**(y//3) + (x//3)]):
#             continue
#         stoku[y][x] = i
#
# for i in range(9):
#     for j in range(9):
#         if stoku[i][j] == 0:
#             num.append(stoku[i][j])
#
# for ri in range(9):
#     arr_li = [False] * 10
#     for rj in range(9):
#         if stoku[ri][rj] == 0:
#             continue
#         if not arr_li[stoku[ri][rj]]:
#             arr_li[stoku[ri][rj]] = True
#
#     for k in range(1, 10):
#         if not arr_li[k]:
#             row_l[ri].append(arr_li[k])
#
# for ci in range(9):
#     arr_li = [False] * 10
#     for cj in range(9):
#         if stoku[cj][ci] == 0:
#             continue
#         if not arr_li[stoku[cj][ci]]:
#             arr_li[stoku[cj][ci]] = True
#
#     for k in range(1, 10):
#         if not arr_li[k]:
#             col_l[ci].append(arr_li[k])
#
# for bi in range(0, 9, 3):
#     arr_li = [False] * 10
#     for bj in range(0, 9, 3):
#         for di in range(3):
#             for dj in range(3):
#                 if stoku[bi + di][bj + dj] == 0:
#                     continue
#                 if not arr_li[stoku[bi + di][bj + dj]]:
#                     arr_li[stoku[bi + di][bj + dj]] = True
#
#         for k in range(1, 10):
#             if not arr_li[k]:
#                 block_l[(3 ** bi) + (bj // 3)].append(arr_li[k])
#
# stuff()

# 두번째 풀이(강의 풀이)
# 일반적인 풀이이지만 시간초과 발생할 수 있음
# 그리고 여기서는 내가 고심했던 0인 값을 넣고 이에대한 뺵트래킹을 어떻게 해야할지 고민을 했는데
# 여기선 레벨이라는 뎊스 개념을 통해 그 값을 관리했음
# def is_possible(y, x, n):
#     global matrix
#
#     for c in range(9):
#         if matrix[y][c] == n:
#             return False
#     for r in range(9):
#         if matrix[r][x] == n:
#             return False
#     for r in range(3):
#         for c in range(3):
#             if matrix[3 * (y // 3) + r][3 *(x // 3) + c] == n:
#                 return False
#
#     return True
#
# def search(lev):
#     global matrix, pos
#
#     #base case
#     if lev == len(pos):
#         for i in range(9):
#             for j in range(9):
#                 print(matrix[i][j], end=" ")
#             print()
#         exit(0)
#
#     y, x = pos[lev]
#
#     #recursive case
#     for n in range(1, 10):
#         if is_possible(y, x, n):
#             matrix[y][x] = n
#             search(lev + 1)
#             matrix[y][x] = 0
#
#
# matrix = [list(map(int, input().split())) for _ in range(9)]
#
# # solve
# pos = []
# for i in range(9):
#     for j in range(9):
#         cur = matrix[i][j]
#         if cur == 0:
#             pos.append((i, j))
#
# search(0)


## 두번쨰 풀이(강의 풀이)
## 셋을 이용한 풀이
## 첫번째 풀이보다 더 빠름, 그 이유는 해당 숫자가 해당 행, 열, 블록에서 사용할 수 있는지 모두 27번씩 구해야하므로
## set 이용한 in 풀이는 해시 함수를 통해서 좀더 빠르게 탐색을 하므로 시간이 전체적으로 단축됨
# def search(lev):
#     global row, col, square, matrix, pos
#
#     # base case
#     if lev == len(pos):
#         for i in range(9):
#             for j in range(9):
#                 print(matrix[i][j], end=' ')
#             print()
#         exit(0)
#
#     y, x = pos[lev]
#
#     # recursive case
#     for n in range(1, 10):
#         if (n not in row[y]) and (n not in col[x]) and (n not in square[y // 3][x // 3]):
#             row[y].add(n)
#             col[x].add(n)
#             square[y // 3][x // 3].add(n)
#             matrix[y][x] = n
#
#             search(lev + 1)
#
#             # 만약 해당 숫자로 결과 도달을 못했을 때 값 원상 복귀
#             matrix[y][x] = 0
#             square[y // 3][x // 3].remove(n)
#             col[x].remove(n)
#             row[y].remove(n)
#
#
# row = [set() for _ in range(9)]
# col = [set() for _ in range(9)]
# square = [[set() for _ in range(3)] for _ in range(3)]
#
# # input
# matrix = [list(map(int, input().split())) for _ in range(9)]
#
# # solve
# pos = []
# for i in range(9):
#     for j in range(9):
#         cur = matrix[i][j]
#         if cur == 0:
#             pos.append((i, j))
#         else:
#             row[i].add(cur)
#             col[j].add(cur)
#             square[i // 3][j // 3].add(cur)
#
# search(0)

## 세번째 풀이(강의 풀이)
## 리스트를 이용한 풀이
## 두번째 풀이보다 좀 더빠른 풀이
## 탐색을 통한 검색이 아닌 인덱스에 직접 접그하므로 조금 더 빠름
def search(lev):
    global row, col, square, matrix, pos

    # base case
    if lev == len(pos):
        for i in range(9):
            for j in range(9):
                print(matrix[i][j], end=" ")
            print()
        exit()

    y, x = pos[lev]

    # recursive case
    for n in range(1, 10):
        if (not row[y][n]) and (not col[x][n]) and (not square[y // 3][x // 3][n]):
            row[y][n] = col[x][n] = square[y // 3][x // 3][n] = True
            matrix[y][x] = n

            search(lev + 1)

            matrix[y][x] = 0
            row[y][n] = col[x][n] = square[y // 3][x // 3][n] = False


row = [[False] * 10 for _ in range(9)]
col = [[False] * 10 for _ in range(9)]
square = [[[False] * 10 for _ in range(3)] for _ in range(3)]

matrix = [list(map(int, input().split())) for _ in range(9)]

# solve
pos = []
for i in range(9):
    for j in range(9):
        cur = matrix[i][j]
        if cur == 0:
            pos.append((i, j))
        else:
            row[i][cur] = col[j][cur] = square[i // 3][j // 3][cur] = True

search(0)

