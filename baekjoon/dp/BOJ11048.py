# 이동하기
# 실버 2
# 첫번쨰 풀이
# Bottom-up 방식의 dp 테이블 완성하는 방법
# 반복문을 통해서 만들고
# dp 테이블의 전체를 완성해야할 때 좋음
# 인덱스 오류가 발생할 수 있으므로 접근하는 순서에 유의하는 것이 필수
N, M = map(int, input().split())

arr = [[0] + list(map(int, input().split())) for _ in range(N)]
arr = [[0] * (M+1)] + arr

dp = [[0 for _ in range(M + 1)] for _ in range(N+1)]
dp[1][1] = arr[1][1]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = arr[i][j]
        dp[i][j] += max(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

print(dp[N][M])

# 두번째 풀이
# Top-down 방식의 dp 테이블 완성하는 방법
# 큰 부분(구하고자 하는 값)을 기준으로 dp table의 필요한 부분만 구하는 방식
# 재귀함수를 이용
# 순서 고려를 따로 안해도 됨
import sys
sys.setrecursionlimit(1000000)


def func(i, j):
    global arr, dp

    # base case
    if dp[i][j] != -1:
        return dp[i][j]

    # recursive case
    dp[i][j] = max(func(i - 1, j), func(i, j - 1), func(i - 1, j - 1)) + arr[i][j]
    return dp[i][j]


N, M = map(int, input().split())

arr = [[0] + list(map(int, input().split())) for _ in range(N)]
arr = [[0] * (M+1)] + arr

dp = [[-1 for _ in range(M+1)] for _ in range(N + 1)]

for j in range(0, M + 1):
    dp[0][j] = 0

for i in range(0, N + 1):
    dp[i][0] = 0

print(func(N, M))




