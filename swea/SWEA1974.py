# SWEA D2
# 스토쿠 문제
# 첫번째 풀이
# 처음 풀 떄 주어진 조건들을 모두 만족하면서 검사하고 그 형태로 코드를 구현하는 것이 가장 적절
# 그러고 나서 슬라이싱이라든지 그 이후에 최적화 할 수 있는지 확인하는 것이 가장 중요
T = int(input())

def is_ans(stokus):
    stoku = set(range(1, 10))

    for bi in (0, 3, 6):
        for bj in (0, 3, 6):
            block = []
            for di in range(3):
                for dj in range(3):
                    block.append(stokus[bi + di][bj + dj])
            if set(block) != stoku:
                return 0

    for ri in range(9):
        raw = []
        for rj in range(9):
            raw.append(stokus[ri][rj])
        if set(raw) != stoku:
            return 0

    for ci in range(9):
        col = []
        for cj in range(9):
            col.append(stokus[cj][ci])
        if set(col) != stoku:
            return 0

    return 1


for t in range(1, T+1):
    stokus = [list(map(int, input().split())) for _ in range(9)]
    res = is_ans(stokus)

    print(f"#{t} {res}")

## 두번째 풀이
## 파이썬으로써 슬라이싱과 zip()함수를 이용한 풀이
def solve(arr):
    arr_t = list(map(list, zip(*arr)))

    # 각 행마다 모두 한번씩 있는지 확인
    for lst in arr:
        if len(set(lst)) != N:
            return 0

    # 각 열마다 모두 한번씩 있는지 확인
    for lst in arr_t:
        if len(set(lst)) != N:
            return 0

    # 3*3 블록마다 1~9가 모두 한번씩 있는지
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # 슬라이싱으로 한줄에 블록 3개를 더해서 9개를 리스트로 변환
            lst = arr[i][j:j+3] + arr[i+1][j: j+3] + arr[i+2][j: j+3]
            if len(set(lst)) != N:
                return 0

    return 1


T = int(input())
N = 9

for test_case in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = solve(arr)
    print(f'#{test_case}', ans)




