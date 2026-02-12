# 행렬 테두리 회전하기 (오래 걸렸던 문제)
# 처음에 잘못한 점
#   - 종료 조건을 값(temp[0]) 으로 잡아서, 한 바퀴 순회를 좌표/길이로 보장하지 못함
#   - while + if/elif로 방향 전환을 직접 구현하다가 케이스(특히 아랫변) 누락 위험이 있었음
#   - (x1, y1, x2, y2)에서 행(row)·열(col) 의미를 혼동해 인덱싱이 뒤집히는 실수가 있었음 (문제 잘 읽기)
#   - 1칸 회전을 좌표 시작점/for 범위 조절로 처리하려다 모서리 중복·누락이 발생함
#   - 읽기/쓰기에서 방문 좌표 집합과 칸 수가 동일해야 한다는 불변조건을 늦게 잡음
#   - 테두리 길이(2*(w+h)-4) 검증을 초반에 안 해서 디버깅이 길어짐

def solution(rows, columns, queries):
    answer = []

    matrix = [[0] * (columns + 1) for _ in range(rows + 1)]
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            matrix[i][j] = (i - 1) * columns + j

    for k in range(len(queries)):
        answer.append(search_min(queries[k], matrix))

    return answer


def search_min(queries, matrix):
    min_val = int(1e12)
    temp = []

    min_x, min_y, max_x, max_y = queries[1], queries[0], queries[3], queries[2]
    x, y = min_x, min_y

    for i in range(min_x, max_x + 1):
        temp.append(matrix[min_y][i])
        min_val = min(matrix[min_y][i], min_val)

    for i in range(min_y + 1, max_y):
        temp.append(matrix[i][max_x])
        min_val = min(matrix[i][max_x], min_val)

    for i in range(max_x, min_x - 1, -1):
        temp.append(matrix[max_y][i])
        min_val = min(matrix[max_y][i], min_val)

    for i in range(max_y - 1, min_y, -1):
        temp.append(matrix[i][min_x])
        min_val = min(matrix[i][min_x], min_val)

    jump_list = num_jump(temp)
    jump_list.reverse()

    for i in range(min_x, max_x + 1):
        matrix[min_y][i] = jump_list.pop()

    for i in range(min_y + 1, max_y):
        matrix[i][max_x] = jump_list.pop()

    for i in range(max_x, min_x - 1, -1):
        matrix[max_y][i] = jump_list.pop()

    for i in range(max_y - 1, min_y, -1):
        matrix[i][min_x] = jump_list.pop()

    return min_val


def num_jump(arr):
    jump_list = []

    jump_list.append(arr[-1])

    for i in range(len(arr) - 1):
        jump_list.append(arr[i])

    return jump_list

# 두번쨰 풀이
# 스택 자료구조를 활용한 풀이
# 나랑 생각하는 거는 비슷하지만 여기는 나처럼 배열 변수를 하나만 만들었고, 역방향으로 돌리지 않고 값을 저장했음
# 즉 현재위치에 값을 stack에 넣고 그러고 그 전값을 현재 위치에 넣는 식으로 만듬
# 그리고 행렬 초기화도 1-index 대신, 0-index를 사용
def solution(rows, columns, queries):
    answer = []

    board = [[i+(j)*columns for i in range(1, columns+1)] for j in range(rows)]
    # print(board)

    for a,b,c,d in queries:
        stack = []
        r1, c1, r2, c2 = a-1, b-1, c-1, d-1


        for i in range(c1, c2+1):

            stack.append(board[r1][i])
            if len(stack) == 1:
                continue
            else:
                board[r1][i] = stack[-2]


        for j in range(r1+1, r2+1):
            stack.append(board[j][i])
            board[j][i] = stack[-2]

        for k in range(c2-1, c1-1, -1):
            stack.append(board[j][k])
            board[j][k] = stack[-2]

        for l in range(r2-1, r1-1, -1):
            stack.append(board[l][k])
            board[l][k] = stack[-2]

        answer.append(min(stack))


    return answer

# 세번째 풀이 (강의 풀이)
# 시간복잡도 : 최대 (400만)
# 기존의 일차원에서 스왑하는 방식을 사각형으로 확장해서 풀었음
def rotate(y1, x1, y2, x2):
    global matrix

    pos = []
    for x in range(x1, x2 + 1):
        pos.append((y1, x))
    for y in range(y1 + 1, y2 + 1):
        pos.append((y, x2))
    for x in range(x2 - 1, x1 - 1, -1):
        pos.append((y2, x))
    for y in range(y2 - 1, y1, -1):
        pos.append((y, x1))

    n = len(pos)

    for i in range(n - 1, 0, -1):
        ny, nx = pos[i][0], pos[i][1],
        by, bx = pos[i - 1][0], pos[i - 1][1],
        matrix[ny][nx], matrix[by][bx] = matrix[by][bx], matrix[ny][nx]

    return min(matrix[y][x] for y, x in pos)


def solution(rows, columns, queries):

    global matrix

    # create matrix
    matrix = [[0] * columns for _ in range(rows)]
    for y in range(rows):
        for x in range(columns):
            matrix[y][x] = x + y * columns + 1

    # solve
    ans = []
    for y1, x1, y2, x2 in queries:
        ans.append(rotate(y1 - 1, x1 - 1, y2 - 1, x2 - 1,))

    return ans

